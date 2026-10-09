--===================================================================================--
--     MIDNIGHT HUB: CORE OPERATIONS & GAME MODIFICATION MODULE
--===================================================================================--

local Players = game:GetService("Players")
local RunService = game:GetService("RunService")
local UserInputService = game:GetService("UserInputService")
local LocalPlayer = Players.LocalPlayer

-- Global Configuration State (Directly reflects your UI element variables)
local HubConfig = {
    WalkspeedValue = 16,        -- Default Roblox Walkspeed
    JumppowerValue = 50,        -- Default Roblox Jumppower
    InfiniteJumpActive = false, -- Connected to your first switch toggle
    NoclipActive = false,       -- Connected to your third switch toggle
    FlightActive = false,       -- Connected to your second switch toggle
    FlightSpeed = 50            -- Speed velocity for Fly GUI flight
}

-- Safe character checker loop utility
local function getCharacterMetrics()
    local character = LocalPlayer.Character or LocalPlayer.CharacterAdded:Wait()
    local humanoid = character:WaitForChild("Humanoid")
    local rootPart = character:WaitForChild("HumanoidRootPart")
    return character, humanoid, rootPart
end

-- ===================================================================================
-- SYSTEM 1: WALKSPEED & JUMPPOWER CONTINUOUS SETTER
-- ===================================================================================
-- Loops in the background to ensure other game scripts don't override your slider settings
task.spawn(function()
    while true do
        local success, _, humanoid = pcall(getCharacterMetrics)
        if success and humanoid then
            humanoid.WalkSpeed = HubConfig.WalkspeedValue
            humanoid.JumpPower = HubConfig.JumppowerValue
        end
        task.wait(0.1) -- Minimal yield to maintain absolute performance stability
    end
end)

-- ===================================================================================
-- SYSTEM 2: INFINITE JUMP CONTROLLER
-- ===================================================================================
UserInputService.JumpRequest:Connect(function()
    if HubConfig.InfiniteJumpActive then
        local success, _, humanoid = pcall(getCharacterMetrics)
        if success and humanoid then
            -- Changes the active state constraint to force an air jump action
            humanoid:ChangeState(Enum.HumanoidStateType.Jumping)
        end
    end
end)

-- ===================================================================================
-- SYSTEM 3: NOCLIP ENGINE (COLLISION SCANNER)
-- ===================================================================================
-- Uses Stepped heartbeat to disconnect character hitboxes prior to physics processing ticks
RunService.Stepped:Connect(function()
    if HubConfig.NoclipActive then
        local success, character = pcall(function() return LocalPlayer.Character end)
        if success and character then
            for _, part in ipairs(character:GetDescendants()) do
                if part:IsA("BasePart") and part.CanCollide == true then
                    part.CanCollide = false
                end
            end
        end
    end
end)

-- ===================================================================================
-- SYSTEM 4: THE FLIGHT EXTENSION (FLY ENGINE)
-- ===================================================================================
local flightBodyVelocity, flightBodyGyro

local function updateFlightState()
    local success, character, _, rootPart = pcall(getCharacterMetrics)
    if not success or not rootPart then return end

    if HubConfig.FlightActive then
        -- Instantiate physics wrappers to counter the gravity model
        flightBodyGyro = Instance.new("BodyGyro")
        flightBodyGyro.P = 9e4
        flightBodyGyro.maxTorque = Vector3.new(9e9, 9e9, 9e9)
        flightBodyGyro.cframe = rootPart.CFrame
        flightBodyGyro.Parent = rootPart

        flightBodyVelocity = Instance.new("BodyVelocity")
        flightBodyVelocity.velocity = Vector3.new(0, 0.1, 0)
        flightBodyVelocity.maxForce = Vector3.new(9e9, 9e9, 9e9)
        flightBodyVelocity.Parent = rootPart

        -- Flight Movement Tracking Loop
        task.spawn(function()
            local camera = workspace.CurrentCamera
            while HubConfig.FlightActive and character.Parent do
                local movementVector = Vector3.new(0, 0, 0)
                
                -- Detect movement inputs to adjust vector positioning configurations
                if UserInputService:IsKeyDown(Enum.KeyCode.W) then
                    movementVector = movementVector + camera.CFrame.LookVector
                end
                if UserInputService:IsKeyDown(Enum.KeyCode.S) then
                    movementVector = movementVector - camera.CFrame.LookVector
                end
                if UserInputService:IsKeyDown(Enum.KeyCode.A) then
                    movementVector = movementVector - camera.CFrame.RightVector
                end
                if UserInputService:IsKeyDown(Enum.KeyCode.D) then
                    movementVector = movementVector + camera.CFrame.RightVector
                end

                flightBodyGyro.cframe = camera.CFrame
                flightBodyVelocity.velocity = movementVector * HubConfig.FlightSpeed
                task.wait()
            end
        end)
    else
        -- Clean closure of physics wrappers upon setting flight state to false
        if flightBodyVelocity then flightBodyVelocity:Destroy() end
        if flightBodyGyro then flightBodyGyro:Destroy() end
    end
end

-- ===================================================================================
-- INTERACTIVE UI TOGGLE TRIGGERS (How your sliders communicate adjustments)
-- ===================================================================================
-- Expose helper hooks so you can test updates manually inside your mobile terminal
_G.UpdateWalkspeed = function(newSpeed) HubConfig.WalkspeedValue = newSpeed end
_G.UpdateJumppower = function(newPower) HubConfig.JumppowerValue = newPower end
_G.ToggleInfJump  = function(state)    HubConfig.InfiniteJumpActive = state end
_G.ToggleNoclip   = function(state)    HubConfig.NoclipActive = state end

_G.ToggleFlight   = function(state)    
    HubConfig.FlightActive = state 
    updateFlightState()
end

print("⭐ [Midnight Hub]: Functional Mod Scripts loaded cleanly. Environment active.")
