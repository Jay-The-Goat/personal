import customtkinter as ctk

# Configure global UI style palette matching your design layout
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class ScriptHubDashboard(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Window Configurations
        self.title("Midnight Hub Control Center")
        self.geometry("960, 600")
        self.resizable(False, False)
        self.configure(fg_color="#0f1115") # Ultra dark slate canvas background

        # Container state trackers
        self.active_tab_frame = None

        # Build structural shell layout components
        self.build_navigation_and_banner_header()
        
        # Load the overview page immediately upon boot configuration
        self.render_overview_dashboard_page()

    def build_navigation_and_banner_header(self):
        """Assembles the user profile header banner card and navigation tabs."""
        # Main Header Card Container (Dark glass frame)
        self.header_card = ctk.CTkFrame(self, fg_color="#181a21", corner_radius=14, border_width=1, border_color="#262930")
        self.header_card.place(x=20, y=20, width=920, height=100)

        # Avatar placeholder grid node (Simulating your user thumbnail box)
        self.avatar_box = ctk.CTkFrame(self.header_card, fg_color="#22252e", corner_radius=10, width=64, height=64)
        self.avatar_box.place(x=18, y=18)
        
        # Inside decoration simulating your avatar profile shape
        self.avatar_inner = ctk.CTkLabel(self.avatar_box, text="👤", font=ctk.CTkFont(size=28))
        self.avatar_inner.place(relx=0.5, rely=0.5, anchor="center")

        # Greeting text fields
        self.greeting_label = ctk.CTkLabel(
            self.header_card, 
            text="Good evening, CrusherEagle1", 
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#ffffff"
        )
        self.greeting_label.place(x=100, y=24)

        self.version_label = ctk.CTkLabel(
            self.header_card, 
            text="You are using Pre Release [v 0.2.0]", 
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="medium"),
            text_color="#8a8f9d"
        )
        self.version_label.place(x=100, y=52)

        # Integrated Tab Switches (Top-right corner button array)
        self.btn_tab_overview = ctk.CTkButton(
            self.header_card, text="Overview", width=100, height=32, corner_radius=8,
            fg_color="#3b82f6", hover_color="#2563eb", text_color="#ffffff",
            font=ctk.CTkFont(size=12, weight="bold"), command=self.render_overview_dashboard_page
        )
        self.btn_tab_overview.place(x=690, y=34)

        self.btn_tab_mods = ctk.CTkButton(
            self.header_card, text="Modifications", width=100, height=32, corner_radius=8,
            fg_color="#22252e", hover_color="#2d323e", text_color="#ffffff",
            font=ctk.CTkFont(size=12, weight="bold"), command=self.render_modifications_page
        )
        self.btn_tab_mods.place(x=802, y=34)

    def flush_viewport_container(self):
        """Clears out the active page content viewport safely."""
        if self.active_tab_frame:
            self.active_tab_frame.destroy()
        self.active_tab_frame = ctk.CTkFrame(self, fg_color="transparent", width=920, height=440)
        self.active_tab_frame.place(x=20, y=140)

    # =========================================================================
    # TAB 1: OVERVIEW DASHBOARD VIEWPORT (REPLICATES SCREENSHOT 1)
    # =========================================================================
    def render_overview_dashboard_page(self):
        self.flush_viewport_container()
        
        # Toggle structural state layout background focus highlights
        self.btn_tab_overview.configure(fg_color="#3b82f6")
        self.btn_tab_mods.configure(fg_color="#22252e")

        # -------------------------------------------------------------
        # LEFT REGION: SERVER MONITOR PANELS
        # -------------------------------------------------------------
        self.server_panel = ctk.CTkFrame(self.active_tab_frame, fg_color="#14161d", corner_radius=14, border_width=1, border_color="#20232b")
        self.server_panel.place(x=0, y=0, width=480, height=300)

        ctk.CTkLabel(self.server_panel, text="Server", font=ctk.CTkFont(size=16, weight="bold"), text_color="#ffffff").place(x=20, y=15)
        ctk.CTkLabel(self.server_panel, text="Information on the session you're currently in", font=ctk.CTkFont(size=11), text_color="#64748b").place(x=20, y=38)

        # Micro Telemetry Matrix Grid items
        self.create_sub_metric_tile(self.server_panel, "Players", "7 playing", 20, 70, 210, 60)
        self.create_sub_metric_tile(self.server_panel, "Maximum Players", "10 players can join", 250, 70, 210, 60)
        self.create_sub_metric_tile(self.server_panel, "Latency", "70ms", 20, 145, 140, 60)
        self.create_sub_metric_tile(self.server_panel, "Server Region", "DE", 175, 145, 285, 60)
        
        # Glowing Teal Gradient Duration Simulation tile
        self.create_sub_metric_tile(self.server_panel, "In server for", "00:03:13", 20, 220, 180, 60, custom_fg="#112926", label_color="#10b981")
        self.create_sub_metric_tile(self.server_panel, "Diagnostics", "Uptime check active.", 215, 220, 245, 60)

        # Discord Floating Action Card 
        self.discord_panel = ctk.CTkFrame(self.active_tab_frame, fg_color="#181a21", corner_radius=14, border_width=1, border_color="#5865f2")
        self.discord_panel.place(x=0, y=320, width=480, height=100)
        ctk.CTkLabel(self.discord_panel, text="Discord", font=ctk.CTkFont(size=22, weight="bold"), text_color="#ffffff").place(x=25, y=20)
        ctk.CTkLabel(self.discord_panel, text="Tap to join the Discord Server", font=ctk.CTkFont(size=14), text_color="#8a8f9d").place(x=25, y=50)

        # -------------------------------------------------------------
        # RIGHT REGION: BAN STATUS, USER, AND FRIENDS MODULES
        # -------------------------------------------------------------
        # Volcano Executor/Ban Risk Status Box
        self.status_panel = ctk.CTkFrame(self.active_tab_frame, fg_color="#1c1616", corner_radius=14, border_width=1, border_color="#ef4444")
        self.status_panel.place(x=500, y=0, width=420, height=110)
        
        ctk.CTkLabel(self.status_panel, text="Volcano User Status", font=ctk.CTkFont(size=18, weight="bold"), text_color="#ef4444").place(x=25, y=20)
        ctk.CTkLabel(self.status_panel, text="Good Executor. I think u can use all\nScripts here safely with 0% Hub Ban Risk.", 
                     font=ctk.CTkFont(size=13, weight="medium"), text_color="#22c55e", justify="left").place(x=25, y=50)

        # Friends Summary Matrix Block
        self.friends_panel = ctk.CTkFrame(self.active_tab_frame, fg_color="#14161d", corner_radius=14, border_width=1, border_color="#20232b")
        self.friends_panel.place(x=500, y=130, width=420, height=290)

        ctk.CTkLabel(self.friends_panel, text="Friends Status Monitor", font=ctk.CTkFont(size=16, weight="bold"), text_color="#ffffff").place(x=25, y=20)
        ctk.CTkLabel(self.friends_panel, text="Find out what your friends are currently doing", font=ctk.CTkFont(size=11), text_color="#64748b").place(x=25, y=43)

        # Friends Data Blocks
        self.create_sub_metric_tile(self.friends_panel, "In Server", "0 friends", 25, 80, 175, 75, custom_fg="#1c1c16")
        self.create_sub_metric_tile(self.friends_panel, "Offline", "0 friends", 220, 80, 175, 75)
        self.create_sub_metric_tile(self.friends_panel, "Online", "0 friends", 25, 175, 175, 75)
        self.create_sub_metric_tile(self.friends_panel, "All Configurations", "0 friends", 220, 175, 175, 75)

    def create_sub_metric_tile(self, parent, title, body, x, y, w, h, custom_fg="#1e212a", label_color="#a3a3a3"):
        """Utility wrapper to compile consistent metric content frames."""
        tile = ctk.CTkFrame(parent, fg_color=custom_fg, corner_radius=10, border_width=1, border_color="#262a35")
        tile.place(x=x, y=y, width=w, height=h)
        
        lbl_title = ctk.CTkLabel(tile, text=title, font=ctk.CTkFont(size=11, weight="bold"), text_color="#ffffff")
        lbl_title.place(x=15, y=10)
        
        lbl_body = ctk.CTkLabel(tile, text=body, font=ctk.CTkFont(size=12), text_color=label_color)
        lbl_body.place(x=15, y=28)

    # =========================================================================
    # TAB 2: MODIFICATIONS VIEWPORT (REPLICATES SCREENSHOT 2 MATCHING TAB 1 LOOK)
    # =========================================================================
    def render_modifications_page(self):
        self.flush_viewport_container()
        
        # Toggle structural state layouts active focus indicator rings
        self.btn_tab_overview.configure(fg_color="#22252e")
        self.btn_tab_mods.configure(fg_color="#3b82f6")

        # -------------------------------------------------------------
        # LEFT MATRIX COLUMN: SLIDER SETTING ARRAYS
        # -------------------------------------------------------------
        self.slider_panel = ctk.CTkFrame(self.active_tab_frame, fg_color="#14161d", corner_radius=14, border_width=1, border_color="#20232b")
        self.slider_panel.place(x=0, y=0, width=440, height=420)
        
        ctk.CTkLabel(self.slider_panel, text="Character Stat Attributes", font=ctk.CTkFont(size=16, weight="bold"), text_color="#ffffff").place(x=25, y=20)

        # Walkspeed Control Slider Module Card
        self.card_ws = ctk.CTkFrame(self.slider_panel, fg_color="#1e212a", corner_radius=10, border_width=1, border_color="#262a35")
        self.card_ws.place(x=20, y=70, width=400, height=85)
        ctk.CTkLabel(self.card_ws, text="Walkspeed", font=ctk.CTkFont(size=13, weight="bold"), text_color="#ffffff").place(x=20, y=15)
self.lbl_ws_val = ctk.CTkLabel(self.card_ws, text="16", font=ctk.CTkFont(size=13), text_color="#3b82f6")
self.lbl_ws_val.place(x=360, y=15)
self.slider_ws = ctk.CTkSlider(self.card_ws, from_=16, to=250, width=360, height=16, command=lambda v: self.lbl_ws_val.configure(text=str(int(v))))
self.slider_ws.set(16)
self.slider_ws.place(x=20, y=48)
# Jumppower Control Slider Module Card
self.card_jp = ctk.CTkFrame(self.slider_panel, fg_color="#1e212a", corner_radius=10, border_width=1, border_color="#262a35")
self.card_jp.place(x=20, y=175, width=400, height=85)
ctk.CTkLabel(self.card_jp, text="Jumppower", font=ctk.CTkFont(size=13, weight="bold"), text_color="#ffffff").place(x=20, y=15)
self.lbl_jp_val = ctk.CTkLabel(self.card_jp, text="50", font=ctk.CTkFont(size=13), text_color="#3b82f6")
self.lbl_jp_val.place(x=360, y=15)
self.slider_jp = ctk.CTkSlider(self.card_jp, from_=50, to=500, width=360, height=16, command=lambda v: self.lbl_jp_val.configure(text=str(int(v))))
self.slider_jp.set(50)
self.slider_jp.place(x=20, y=48)
# -------------------------------------------------------------
# RIGHT MATRIX COLUMN: FUNCTION TOGGLE ARRAYS
# -------------------------------------------------------------
self.toggle_panel = ctk.CTkFrame(self.active_tab_frame, fg_color="#14161d", corner_radius=14, border_width=1, border_color="#20232b")
self.toggle_panel.place(x=460, y=0, width=460, height=420)
ctk.CTkLabel(self.toggle_panel, text="Automation Systems", font=ctk.CTkFont(size=16, weight="bold"), text_color="#ffffff").place(x=25, y=20)
# Infinite Jump Function Card
self.create_functional_switch_row(
self.toggle_panel, "Infinite Jump", "Allows you jump in the air without resetting ground ticks.", 20, 70
)
# Fly Gui Toggle Card
self.create_functional_switch_row(
self.toggle_panel, "Fly Gui Layout", "Custom-made flight telemetry interface matching Midnight Hub aesthetics.", 20, 160
)
# Noclip Feature Toggle Card
self.create_functional_switch_row(
self.toggle_panel, "Noclip Engine", "Disables engine part collisions to pass safely through workspace solid walls.", 20, 250
)
def create_functional_switch_row(self, parent, name, desc, x, y):
"""Assembles unified slider/toggle switch item frame controls inside tab environments."""
row_card = ctk.CTkFrame(parent, fg_color="#1e212a", corner_radius=10, border_width=1, border_color="#262a35")
row_card.place(x=x, y=y, width=420, height=75)
ctk.CTkLabel(row_card, text=name, font=ctk.CTkFont(size=13, weight="bold"), text_color="#ffffff").place(x=20, y=12)
ctk.CTkLabel(row_card, text=desc, font=ctk.CTkFont(size=11), text_color="#64748b").place(x=20, y=36)
sw_item = ctk.CTkSwitch(row_card, text="", width=45, height=24, progress_color="#3b82f6")
sw_item.place(x=350, y=14)
if name == "main":
app = ScriptHubDashboard()
app.mainloop()