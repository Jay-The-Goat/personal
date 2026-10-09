import customtkinter as ctk

# Configure global dark theme properties to mirror your dashboard images
ctk.set_appearance_mode("Dark")
ctk.set_default_color_theme("blue")

class MidnightHubUIDesigner(ctk.CTk):
    def __init__(self):
        super().__init__()

        # Desktop Window Configurations
        self.title("Midnight Hub - Developer UI Control Center")
        self.geometry("960x600")
        self.resizable(False, False)
        self.configure(fg_color="#0f1115") # Match your first image's dark backdrop

        # Active view container tracker
        self.current_viewport = None

        # Assemble fixed header panel structure
        self.initialize_header_navigation()
        
        # Load the Overview Page as the initial view
        self.switch_to_overview_page()

    def initialize_header_navigation(self):
        """Builds the main user header block card containing tabs and versioning text."""
        # Top Header Background Card
        self.header_card = ctk.CTkFrame(self, fg_color="#181a21", corner_radius=14, border_width=1, border_color="#262930")
        self.header_card.place(x=20, y=20, width=920, height=100)

        # Avatar Frame Layout Box
        self.avatar_frame = ctk.CTkFrame(self.header_card, fg_color="#22252e", corner_radius=10, width=64, height=64)
        self.avatar_frame.place(x=18, y=18)
        self.avatar_label = ctk.CTkLabel(self.avatar_frame, text="👤", font=ctk.CTkFont(size=28))
        self.avatar_label.place(relx=0.5, rely=0.5, anchor="center")

        # Configuration Status Strings
        self.user_heading = ctk.CTkLabel(
            self.header_card, 
            text="Good evening, CrusherEagle1", 
            font=ctk.CTkFont(family="Segoe UI", size=18, weight="bold"),
            text_color="#ffffff"
        )
        self.user_heading.place(x=100, y=24)

        self.sub_heading = ctk.CTkLabel(
            self.header_card, 
            text="You are using Pre Release [v 0.2.0]", 
            font=ctk.CTkFont(family="Segoe UI", size=13, weight="medium"),
            text_color="#8a8f9d"
        )
        self.sub_heading.place(x=100, y=52)

        # Navigation Controls (Top Right Tabs Array)
        self.btn_nav_overview = ctk.CTkButton(
            self.header_card, text="Overview", width=100, height=32, corner_radius=8,
            fg_color="#3b82f6", hover_color="#2563eb", text_color="#ffffff",
            font=ctk.CTkFont(size=12, weight="bold"), command=self.switch_to_overview_page
        )
        self.btn_nav_overview.place(x=690, y=34)

        self.btn_nav_mods = ctk.CTkButton(
            self.header_card, text="Modifications", width=100, height=32, corner_radius=8,
            fg_color="#22252e", hover_color="#2d323e", text_color="#ffffff",
            font=ctk.CTkFont(size=12, weight="bold"), command=self.switch_to_modifications_page
        )
        self.btn_nav_mods.place(x=802, y=34)

    def wipe_viewport(self):
        """Clears old viewport containers before swapping script pages."""
        if self.current_viewport:
            self.current_viewport.destroy()
        self.current_viewport = ctk.CTkFrame(self, fg_color="transparent", width=920, height=440)
        self.current_viewport.place(x=20, y=140)

    # =========================================================================
    # TAB 1: OVERVIEW PAGE (Replicates Screenshot 1 Layout Panels)
    # =========================================================================
    def switch_to_overview_page(self):
        self.wipe_viewport()
        self.btn_nav_overview.configure(fg_color="#3b82f6")
        self.btn_nav_mods.configure(fg_color="#22252e")

        # ----------------- LEFT SIDE CONTEXT BLOCKS -----------------
        # Main Server Info Frame Container
        server_box = ctk.CTkFrame(self.current_viewport, fg_color="#14161d", corner_radius=14, border_width=1, border_color="#20232b")
        server_box.place(x=0, y=0, width=480, height=300)

        ctk.CTkLabel(server_box, text="Server", font=ctk.CTkFont(size=16, weight="bold"), text_color="#ffffff").place(x=20, y=15)
        ctk.CTkLabel(server_box, text="Information on the session you're currently in", font=ctk.CTkFont(size=11), text_color="#64748b").place(x=20, y=38)

        # Micro Server Metric Tiles
        self.create_data_tile(server_box, "Players", "7 playing", 20, 70, 210, 60)
        self.create_data_tile(server_box, "Maximum Players", "10 players can join", 250, 70, 210, 60)
        self.create_data_tile(server_box, "Latency", "70ms", 20, 145, 140, 60)
        self.create_data_tile(server_box, "Server Region", "DE", 175, 145, 285, 60)
        self.create_data_tile(server_box, "In server for", "00:03:13", 20, 220, 180, 60, bg="#112926", txt_clr="#10b981")
        self.create_data_tile(server_box, "Diagnostics", "Uptime monitor safe.", 215, 220, 245, 60)

        # Discord Card Panel
        discord_box = ctk.CTkFrame(self.current_viewport, fg_color="#181a21", corner_radius=14, border_width=1, border_color="#5865f2")
        discord_box.place(x=0, y=320, width=480, height=100)
        ctk.CTkLabel(discord_box, text="Discord", font=ctk.CTkFont(size=22, weight="bold"), text_color="#ffffff").place(x=25, y=20)
        ctk.CTkLabel(discord_box, text="Tap to join the Discord Server", font=ctk.CTkFont(size=14), text_color="#8a8f9d").place(x=25, y=50)

        # ----------------- RIGHT SIDE CONTEXT BLOCKS -----------------
        # Top-Right Volcano Executor Info Panel
        volcano_box = ctk.CTkFrame(self.current_viewport, fg_color="#1c1616", corner_radius=14, border_width=1, border_color="#ef4444")
        volcano_box.place(x=500, y=0, width=420, height=110)
        ctk.CTkLabel(volcano_box, text="Volcano User", font=ctk.CTkFont(size=18, weight="bold"), text_color="#ef4444").place(x=25, y=20)
        ctk.CTkLabel(volcano_box, text="Good Executor. I think u can use all\nScripts here.", 
                     font=ctk.CTkFont(size=13, weight="medium"), text_color="#22c55e", justify="left").place(x=25, y=50)

        # Bottom-Right Friends Matrix Container Panel
        friends_box = ctk.CTkFrame(self.current_viewport, fg_color="#14161d", corner_radius=14, border_width=1, border_color="#20232b")
        friends_box.place(x=500, y=130, width=420, height=290)
        ctk.CTkLabel(friends_box, text="Friends", font=ctk.CTkFont(size=16, weight="bold"), text_color="#ffffff").place(x=25, y=20)
        ctk.CTkLabel(friends_box, text="Find out what your friends are currently doing", font=ctk.CTkFont(size=11), text_color="#64748b").place(x=25, y=43)

        # Sub-Friend Counters (Styled to match screenshot 1)
        self.create_data_tile(friends_box, "In Server", "0 friends", 25, 80, 175, 75, bg="#1c1c16")
        self.create_data_tile(friends_box, "Offline", "0 friends", 220, 80, 175, 75)
        self.create_data_tile(friends_box, "Online", "0 friends", 25, 175, 175, 75)
        self.create_data_tile(friends_box, "All", "0 friends", 220, 175, 175, 75)

    def create_data_tile(self, parent, title, status, x, y, w, h, bg="#1e212a", txt_clr="#a3a3a3"):
        """Compiles clean rounded metric boxes mimicking card items inside screenshot 1."""
        tile = ctk.CTkFrame(parent, fg_color=bg, corner_radius=10, border_width=1, border_color="#262a35")
        tile.place(x=x, y=y, width=w, height=h)
        ctk.CTkLabel(tile, text=title, font=ctk.CTkFont(size=11, weight="bold"), text_color="#ffffff").place(x=15, y=10)
        ctk.CTkLabel(tile, text=status, font=ctk.CTkFont(size=12), text_color=txt_clr).place(x=15, y=28)

    # =========================================================================
    # TAB 2: MODIFICATIONS PAGE (Replicates Screenshot 2 styled like Page 1)
    # =========================================================================
    def switch_to_modifications_page(self):
        self.wipe_viewport()
        self.btn_nav_overview.configure(fg_color="#22252e")
        self.btn_nav_mods.configure(fg_color="#3b82f6")

        # ----------------- LEFT SIDE: ADJUSTMENT SLIDERS -----------------
        sliders_panel = ctk.CTkFrame(self.current_viewport, fg_color="#14161d", corner_radius=14, border_width=1, border_color="#20232b")
        sliders_panel.place(x=0, y=0, width=440, height=420)
        
        ctk.CTkLabel(sliders_panel, text="Character Settings", font=ctk.CTkFont(size=16, weight="bold"), text_color="#ffffff").place(x=25, y=20)

        # Walkspeed Slider Module Card
        ws_card = ctk.CTkFrame(sliders_panel, fg_color="#1e212a", corner_radius=10, border_width=1, border_color="#262a35")
        ws_card.place(x=20, y=70, width=400, height=85)
        ctk.CTkLabel(ws_card, text="Walkspeed", font=ctk.CTkFont(size=13, weight="bold"), text_color="#ffffff").place(x=20, y=15)
        self.ws_val = ctk.CTkLabel(ws_card, text="16", font=ctk.CTkFont(size=13), text_color="#3b82f6")
        self.ws_val.place(x=360, y=15)
        self.ws_slider = ctk.CTkSlider(ws_card, from_=16, to=250, width=360, command=lambda v: self.ws_val.configure(text=str(int(v))))
        self.ws_slider.set(16)
        self.ws_slider.place(x=20, y=48)

        # Jumppower Slider Module Card
        jp_card = ctk.CTkFrame(sliders_panel, fg_color="#1e212a", corner_radius=10, border_width=1, border_color="#262a35")
        jp_card.place(x=20, y=175, width=400, height=85)
        ctk.CTkLabel(jp_card, text="Jumppower", font=ctk.CTkFont(size=13, weight="bold"), text_color="#ffffff").place(x=20, y=15)
        self.jp_val = ctk.CTkLabel(jp_card, text="50", font=ctk.CTkFont(size=13), text_color="#3b82f6")
        self.jp_val.place(x=360, y=15)
        self.jp_slider = ctk.CTkSlider(jp_card, from_=50, to=500, width=360, command=lambda v: self.jp_val.configure(text=str(int(v))))
        self.jp_slider.set(50)
        self.jp_slider.place(x=20, y=48)

        # ----------------- RIGHT SIDE: AUTOMATION TOGGLES -----------------
toggles_panel = ctk.CTkFrame(self.current_viewport, fg_color="#14161d", corner_radius=14, border_width=1, border_color="#20232b")
toggles_panel.place(x=460, y=0, width=460, height=420)
ctk.CTkLabel(toggles_panel, text="Automation Toggles", font=ctk.CTkFont(size=16, weight="bold"), text_color="#ffffff").place(x=25, y=20)
# Infinite Jump Row Card
self.create_toggle_row(toggles_panel, "Infinite Jump", "Allows you jump in the air", 20, 70)
# Fly Gui Row Card (Inspired by fly GUI V3 description)
self.create_toggle_row(toggles_panel, "Fly Gui", "Custom-made fly GUI to match the theme of Midnight Hub", 20, 160)
# Noclip Row Card
self.create_toggle_row(toggles_panel, "Noclip", "Allows your character to pass through game assets and walls", 20, 250)
def create_toggle_row(self, parent, name, desc, x, y):
"""Assembles a clean toggle list item styled identically to the first dashboard panels."""
row_frame = ctk.CTkFrame(parent, fg_color="#1e212a", corner_radius=10, border_width=1, border_color="#262a35")
row_frame.place(x=x, y=y, width=420, height=75)
ctk.CTkLabel(row_frame, text=name, font=ctk.CTkFont(size=13, weight="bold"), text_color="#ffffff").place(x=20, y=12)
ctk.CTkLabel(row_frame, text=desc, font=ctk.CTkFont(size=11), text_color="#64748b").place(x=20, y=36)
toggle_switch = ctk.CTkSwitch(row_frame, text="", width=45, height=24, progress_color="#3b82f6")
toggle_switch.place(x=350, y=14)
if name == "main":
app = MidnightHubUIDesigner()
app.mainloop()