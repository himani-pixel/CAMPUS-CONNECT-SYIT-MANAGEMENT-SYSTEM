import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from datetime import datetime
import random
import math

class Node:
    """Node for singly linked list"""
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    """Singly Linked List for announcements"""
    def __init__(self):
        self.head = None
    
    def add_announcement(self, message):
        """Add announcement to the front (most recent first)"""
        new_node = Node(message)
        new_node.next = self.head
        self.head = new_node
    
    def display_announcements(self):
        """Display all announcements"""
        announcements = []
        current = self.head
        count = 1
        while current:
            announcements.append(f"{count}. {current.data}")
            current = current.next
            count += 1
        return announcements

class Stack:
    """Stack for assignment submission history"""
    def __init__(self):
        self.items = []
    
    def push(self, item):
        """Push assignment to stack"""
        self.items.append(item)
    
    def pop(self):
        """Pop assignment from stack"""
        if not self.is_empty():
            return self.items.pop()
        return None
    
    def is_empty(self):
        """Check if stack is empty"""
        return len(self.items) == 0
    
    def display_stack(self):
        """Display submission history"""
        submissions = []
        if not self.is_empty():
            for i, item in enumerate(reversed(self.items), 1):
                submissions.append(f"{i}. {item}")
        return submissions

class Queue:
    """Queue for lab equipment booking"""
    def __init__(self):
        self.items = []
    
    def enqueue(self, item):
        """Add student to waiting list"""
        self.items.append(item)
    
    def dequeue(self):
        """Remove student from waiting list"""
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def is_empty(self):
        """Check if queue is empty"""
        return len(self.items) == 0
    
    def size(self):
        """Get queue size"""
        return len(self.items)
    
    def display_queue(self):
        """Display waiting list"""
        waiting_list = []
        if not self.is_empty():
            for i, student in enumerate(self.items, 1):
                waiting_list.append(f"{i}. {student}")
        return waiting_list

class AnimatedGradientLabel(tk.Label):
    """Animated gradient label for eye-catching headers"""
    def __init__(self, parent, text, **kwargs):
        super().__init__(parent, text=text, font=('Arial', 28, 'bold'), **kwargs)
        self.colors = ['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD']
        self.color_index = 0
        self.animate()
    
    def animate(self):
        """Animate the text color"""
        if self.winfo_exists():  # Check if widget still exists
            self.config(fg=self.colors[self.color_index])
            self.color_index = (self.color_index + 1) % len(self.colors)
            self.after(200, self.animate)

class Particle:
    """Particle for background animation"""
    def __init__(self, canvas, width, height):
        self.canvas = canvas
        self.width = width
        self.height = height
        self.x = random.randint(0, width)
        self.y = random.randint(0, height)
        self.size = random.randint(2, 5)
        self.speed_x = random.uniform(-0.5, 0.5)
        self.speed_y = random.uniform(-0.5, 0.5)
        self.color = random.choice(['#FF6B6B', '#4ECDC4', '#45B7D1', '#96CEB4', '#FFEAA7', '#DDA0DD'])
        self.particle = self.canvas.create_oval(
            self.x, self.y, self.x + self.size, self.y + self.size,
            fill=self.color, outline=''
        )
    
    def move(self):
        """Move the particle"""
        self.x += self.speed_x
        self.y += self.speed_y
        
        # Bounce off edges
        if self.x <= 0 or self.x >= self.width:
            self.speed_x *= -1
        if self.y <= 0 or self.y >= self.height:
            self.speed_y *= -1
        
        self.canvas.coords(self.particle, self.x, self.y, self.x + self.size, self.y + self.size)

class SimpleGradientFrame(tk.Frame):
    """Simplified gradient frame that actually works"""
    def __init__(self, parent, color, **kwargs):
        super().__init__(parent, bg=color, **kwargs)

class ModernButton(tk.Button):
    """Modern animated button with hover effects"""
    def __init__(self, parent, text, command, **kwargs):
        # Default styling
        defaults = {
            'bg': '#FF6B6B',
            'fg': 'white',
            'font': ('Arial', 14, 'bold'),
            'relief': 'raised',
            'bd': 0,
            'padx': 20,
            'pady': 12,
            'cursor': 'hand2'
        }
        defaults.update(kwargs)
        
        super().__init__(parent, text=text, command=command, **defaults)
        
        # Bind events for hover effects
        self.bind('<Enter>', self._on_enter)
        self.bind('<Leave>', self._on_leave)
        self.bind('<ButtonPress-1>', self._on_press)
        self.bind('<ButtonRelease-1>', self._on_release)
        
        self.original_bg = self['bg']
        self.hover_bg = self._adjust_color(self.original_bg, -20)  # Darker on hover
    
    def _on_enter(self, event):
        """Mouse enter event"""
        self.config(bg=self.hover_bg)
    
    def _on_leave(self, event):
        """Mouse leave event"""
        self.config(bg=self.original_bg)
    
    def _on_press(self, event):
        """Mouse press event"""
        self.config(relief='sunken')
    
    def _on_release(self, event):
        """Mouse release event"""
        self.config(relief='raised')
    
    def _adjust_color(self, hex_color, amount):
        """Adjust color brightness"""
        try:
            hex_color = hex_color.lstrip('#')
            r = max(0, min(255, int(hex_color[0:2], 16) + amount))
            g = max(0, min(255, int(hex_color[2:4], 16) + amount))
            b = max(0, min(255, int(hex_color[4:6], 16) + amount))
            return f'#{r:02x}{g:02x}{b:02x}'
        except:
            return hex_color  # Return original if error

class CampusConnectGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎓 CAMPUS CONNECT - SYIT MANAGEMENT SYSTEM 🎓")
        self.root.geometry("1400x900")
        self.root.configure(bg='#1a1a2e')
        
        # Enhanced vibrant theme settings
        self.dark_mode = True
        self.theme_colors = {
            'dark': {
                'bg': '#1a1a2e',
                'fg': '#ffffff',
                'header_bg': '#16213e',
                'card_bg': '#0f3460',
                'button_bg': '#e94560',
                'button_active': '#c13651',
                'entry_bg': '#16213e',
                'entry_fg': '#ffffff',
                'accent': '#f39c12',
                'success': '#2ecc71',
                'warning': '#f1c40f',
                'danger': '#e74c3c',
                'gradient1': '#1a1a2e',
                'gradient2': '#16213e'
            },
            'light': {
                'bg': '#ecf0f1',
                'fg': '#2c3e50',
                'header_bg': '#3498db',
                'card_bg': '#ffffff',
                'button_bg': '#2980b9',
                'button_active': '#1f618d',
                'entry_bg': '#ffffff',
                'entry_fg': '#2c3e50',
                'accent': '#f39c12',
                'success': '#27ae60',
                'warning': '#f1c40f',
                'danger': '#e74c3c',
                'gradient1': '#ecf0f1',
                'gradient2': '#3498db'
            }
        }
        
        # Initialize data structures
        self.students = {
            "S001": {"name": "Himani Malankar", "phone": "9876512345", "year": "SY", "department": "IT"},
            "S002": {"name": "Sachin Singh", "phone": "9876523456", "year": "SY", "department": "IT"},
            "S003": {"name": "Shubham Mandavkar", "phone": "9876534567", "year": "SY", "department": "IT"},
            "S004": {"name": "Harshita Kanojia", "phone": "9876545678", "year": "SY", "department": "IT"},
            "S005": {"name": "Omkar Sawant", "phone": "9876556789", "year": "SY", "department": "IT"},
            "S006": {"name": "Saqlain Khan", "phone": "9876567890", "year": "SY", "department": "IT"},
            "S007": {"name": "Rites Chaubey", "phone": "9876578901", "year": "SY", "department": "IT"}
        }
        
        self.announcements = LinkedList()
        self.submission_stack = Stack()
        self.lab_queue = Queue()
        
        # IT-specific lab equipment
        self.lab_equipment = {
            "Computer Systems": [
                "High-Performance Desktop (i9, 32GB RAM)",
                "Gaming PC (RTX 4080, 16GB RAM)",
                "Mac Studio (M2 Ultra, 64GB RAM)",
                "Linux Workstation (Ubuntu Server)",
                "Windows Server Machine"
            ],
            "Networking": [
                "Cisco Router & Switch Lab Kit",
                "Network Simulation Workstation",
                "Wireless Networking Testbed",
                "Network Security Analyzer"
            ],
            "Development": [
                "Dual Monitor Programming Station",
                "Mobile Development Test Devices",
                "Web Development Server",
                "Database Server (MySQL/PostgreSQL)"
            ],
            "Specialized Hardware": [
                "Raspberry Pi Cluster",
                "Arduino Development Kits",
                "3D Printer (Creality Ender 3)",
                "VR Development Station",
                "IoT Sensor Kit"
            ]
        }
        
        # Fixed timetable - added missing commas
        self.timetable = [
            ["07:30-08:30", "", "", "CC Sports (Mr. Deepak) R.209", "", "", ""],
            ["08:30-09:30", "", "", "Python Programming (Asst. Prof. Sneha) R.004", 
             "Hindi Bhasha (Asst. Prof. Mukesh) R.209", "", "Applied Mathematics (Asst. Prof. Rohini) R.208"],
            ["09:30-10:30", "", "", "", "", "", ""],
            ["10:30-10:50", "BREAK", "BREAK", "BREAK", "BREAK", "BREAK", "BREAK"],
            ["10:50-11:50", "Data Structures (Asst. Prof. Sumit) R.208", 
             "Data Structures (Asst. Prof. Sumit) R.208", 
             "Operating System (Asst. Prof. Chetana) R.208", 
             "Hindi Bhasha (Asst. Prof. Mukesh) R.209", 
             "Library", 
             "Introduction to Geoinformatics (Asst.Prof. Sneha) R.004"],
            ["11:50-12:50", "Operating System (Asst. Prof. Chetana) R.208", 
             "Applied Mathematics (Asst. Prof. Rohini) R.208", 
             "Field Project (Asst. Prof. Sneha) R.208", 
             "Python Programming (Asst. Prof. Sneha) R.004", 
             "Introduction to Geoinformatics (Asst.Prof. Sneha) R.004", 
             "Field Project (Asst. Prof. Sumit) R.004"],
            ["13:00-14:00", "Scala Prog. Practical (Asst. Prof. Rohini) IT Lab", 
             "Python Practical (Asst. Prof. Sneha) IT Lab", 
             "", 
             "Data Structures Practical (Asst. Prof. Sumit) IT Lab", 
             "Python for DS Practical (Asst. Prof. Sumit) IT Lab", 
             ""]
        ]
        
        self.days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
        self.grades = [85, 92, 78, 65, 88, 95, 72, 81]
        self.current_user = None
        
        # Animation variables
        self.particles = []
        
        # Add sample data
        self.add_sample_data()
        
        # Configure styles
        self.configure_styles()
        
        # Create animated background
        self.create_animated_background()
        
        # Create GUI
        self.create_login_screen()
    
    def create_animated_background(self):
        """Create animated background with particles"""
        self.bg_canvas = tk.Canvas(self.root, bg=self.theme_colors['dark']['bg'], highlightthickness=0)
        self.bg_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Create particles after window is rendered
        self.root.after(100, self.create_particles)
        
    def create_particles(self):
        """Create animated particles"""
        try:
            width = self.root.winfo_width()
            height = self.root.winfo_height()
            
            if width > 1 and height > 1:
                self.bg_canvas.delete("all")
                self.particles = []
                
                for _ in range(15):  # Reduced for better performance
                    self.particles.append(Particle(self.bg_canvas, width, height))
                
                self.animate_particles()
        except (tk.TclError, AttributeError):
            pass  # Window might be closed
    
    def animate_particles(self):
        """Animate particles"""
        try:
            if hasattr(self, 'bg_canvas') and self.bg_canvas.winfo_exists():
                for particle in self.particles:
                    particle.move()
                
                self.root.after(50, self.animate_particles)
        except (tk.TclError, AttributeError):
            pass  # Window might be closed
    
    def configure_styles(self):
        """Configure ttk styles for modern look"""
        try:
            style = ttk.Style()
            style.theme_use('clam')
            
            # Configure custom styles with vibrant colors
            style.configure('Custom.TNotebook', 
                           background=self.theme_colors['dark']['bg'])
            style.configure('Custom.TNotebook.Tab', 
                           background=self.theme_colors['dark']['card_bg'],
                           foreground=self.theme_colors['dark']['fg'],
                           padding=[20, 10],
                           font=('Arial', 12, 'bold'))
            
            style.map('Custom.TNotebook.Tab',
                     background=[('selected', self.theme_colors['dark']['accent'])],
                     foreground=[('selected', 'white')])
        except:
            pass  # Style configuration might fail on some systems
    
    def create_gradient_header(self, parent, text, gradient_color):
        """Create a simplified gradient header"""
        header = SimpleGradientFrame(parent, gradient_color, height=80)
        header.pack(fill='x', padx=10, pady=10)
        
        title = tk.Label(header, text=text, bg=gradient_color, fg='white', 
                        font=('Arial', 24, 'bold'), pady=20)
        title.pack(expand=True)
        
        return header
    
    def create_login_screen(self):
        """Create vibrant login screen"""
        self.clear_screen()
        
        # Main container with solid background
        main_frame = SimpleGradientFrame(self.root, self.theme_colors['dark']['bg'])
        main_frame.pack(fill='both', expand=True)
        
        # Login container
        login_container = SimpleGradientFrame(main_frame, self.theme_colors['dark']['card_bg'], 
                                            height=500, width=600)
        login_container.place(relx=0.5, rely=0.5, anchor='center')
        login_container.pack_propagate(False)
        
        # Animated title
        title = tk.Label(login_container, text="🎓 CAMPUS CONNECT 🎓", 
                        bg=self.theme_colors['dark']['card_bg'], 
                        fg=self.theme_colors['dark']['accent'], 
                        font=('Arial', 28, 'bold'))
        title.pack(pady=30)
        
        subtitle = tk.Label(login_container, text="SYIT MANAGEMENT SYSTEM", 
                           bg=self.theme_colors['dark']['card_bg'], 
                           fg='white', font=('Arial', 18, 'bold'))
        subtitle.pack(pady=5)
        
        # Login form
        form_container = SimpleGradientFrame(login_container, self.theme_colors['dark']['card_bg'])
        form_container.pack(pady=30, padx=50, fill='both', expand=True)
        
        tk.Label(form_container, text="Student ID:", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 16, 'bold')).pack(pady=15)
        
        self.login_entry = tk.Entry(form_container, width=25, font=('Arial', 14),
                                   bg=self.theme_colors['dark']['entry_bg'],
                                   fg=self.theme_colors['dark']['entry_fg'],
                                   insertbackground='white')
        self.login_entry.pack(pady=10)
        self.login_entry.focus()
        
        # Bind Enter key to login
        self.login_entry.bind('<Return>', lambda e: self.handle_login())
        
        # Modern login button
        login_btn = ModernButton(form_container, text="🚀 LOGIN", command=self.handle_login,
                                bg=self.theme_colors['dark']['accent'],
                                fg='white', font=('Arial', 16, 'bold'),
                                padx=30, pady=15)
        login_btn.pack(pady=20)
        
        # Signup button
        signup_btn = ModernButton(form_container, text="✨ New Student? Sign Up", 
                                 command=self.create_signup_screen,
                                 bg=self.theme_colors['dark']['success'],
                                 fg='white', font=('Arial', 14, 'bold'))
        signup_btn.pack(pady=10)
        
        # Student IDs hint
        hint_label = tk.Label(form_container, text="Try: S001 to S007", 
                             bg=self.theme_colors['dark']['card_bg'], fg='#FFD700',
                             font=('Arial', 12, 'bold'))
        hint_label.pack(pady=10)

    def create_signup_screen(self):
        """Create student registration screen"""
        self.clear_screen()
        
        main_frame = SimpleGradientFrame(self.root, self.theme_colors['dark']['bg'])
        main_frame.pack(fill='both', expand=True)
        
        signup_frame = SimpleGradientFrame(main_frame, self.theme_colors['dark']['card_bg'], 
                                         height=550, width=550)
        signup_frame.place(relx=0.5, rely=0.5, anchor='center')
        signup_frame.pack_propagate(False)
        
        tk.Label(signup_frame, text="🎓 STUDENT REGISTRATION 🎓", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg=self.theme_colors['dark']['accent'], 
                font=('Arial', 24, 'bold')).pack(pady=20)
        
        # Registration form
        form_frame = SimpleGradientFrame(signup_frame, self.theme_colors['dark']['card_bg'])
        form_frame.pack(pady=20, padx=30, fill='both', expand=True)
        
        # Form fields
        fields = [
            ("Full Name:", "name_entry"),
            ("Phone Number:", "phone_entry"), 
            ("Student ID:", "id_entry"),
            ("Year:", "year_entry"),
            ("Department:", "dept_entry")
        ]
        
        self.signup_entries = {}
        
        for i, (label, key) in enumerate(fields):
            tk.Label(form_frame, text=label, bg=self.theme_colors['dark']['card_bg'],
                    fg='white', font=('Arial', 12)).grid(row=i, column=0, sticky='w', pady=10, padx=10)
            
            entry = tk.Entry(form_frame, width=25, font=('Arial', 12),
                            bg=self.theme_colors['dark']['entry_bg'],
                            fg=self.theme_colors['dark']['entry_fg'],
                            insertbackground='white')
            entry.grid(row=i, column=1, pady=10, padx=10)
            self.signup_entries[key] = entry
        
        # Set default values
        self.signup_entries['year_entry'].insert(0, "SY")
        self.signup_entries['dept_entry'].insert(0, "IT")
        
        # Buttons
        btn_frame = SimpleGradientFrame(form_frame, self.theme_colors['dark']['card_bg'])
        btn_frame.grid(row=5, column=0, columnspan=2, pady=20)
        
        register_btn = ModernButton(btn_frame, text="📝 REGISTER", command=self.handle_signup,
                                  bg=self.theme_colors['dark']['success'],
                                  fg='white', font=('Arial', 14, 'bold'))
        register_btn.pack(side='left', padx=10)
        
        back_btn = ModernButton(btn_frame, text="↩️ BACK", command=self.create_login_screen,
                               bg=self.theme_colors['dark']['danger'],
                               fg='white', font=('Arial', 14, 'bold'))
        back_btn.pack(side='left', padx=10)
    
    def handle_signup(self):
        """Handle student registration"""
        try:
            name = self.signup_entries['name_entry'].get().strip()
            phone = self.signup_entries['phone_entry'].get().strip()
            student_id = self.signup_entries['id_entry'].get().strip().upper()
            year = self.signup_entries['year_entry'].get().strip()
            dept = self.signup_entries['dept_entry'].get().strip()
            
            if not all([name, phone, student_id, year, dept]):
                messagebox.showerror("Error", "Please fill all fields!")
                return
            
            if not student_id.startswith('S'):
                messagebox.showerror("Error", "Student ID must start with 'S'!")
                return
            
            if student_id in self.students:
                messagebox.showerror("Error", "Student ID already exists!")
                return
            
            self.students[student_id] = {
                "name": name, "phone": phone, "year": year, "department": dept
            }
            
            messagebox.showinfo("Success", f"Welcome {name}! Registration successful!")
            self.create_login_screen()
            
        except Exception as e:
            messagebox.showerror("Error", f"Registration failed: {str(e)}")
    
    def handle_login(self):
        """Handle login attempt"""
        student_id = self.login_entry.get().strip().upper()
        
        if student_id in self.students:
            self.current_user = self.students[student_id]
            self.current_user['id'] = student_id
            messagebox.showinfo("Success", f"Welcome back, {self.current_user['name']}!")
            self.create_main_dashboard()
        else:
            messagebox.showerror("Error", "Invalid Student ID! Try S001 to S007")

    def create_main_dashboard(self):
        """Create vibrant main dashboard"""
        self.clear_screen()
        
        # Header
        header_frame = SimpleGradientFrame(self.root, self.theme_colors['dark']['header_bg'], height=100)
        header_frame.pack(fill='x', padx=10, pady=10)
        
        header_content = SimpleGradientFrame(header_frame, self.theme_colors['dark']['header_bg'])
        header_content.pack(fill='both', expand=True, padx=20, pady=10)
        
        title = tk.Label(header_content, text="🎓 CAMPUS CONNECT - SYIT MANAGEMENT SYSTEM 🎓",
                        bg=self.theme_colors['dark']['header_bg'], 
                        fg=self.theme_colors['dark']['accent'], 
                        font=('Arial', 20, 'bold'))
        title.pack(side='left')
        
        # User info and controls
        control_frame = SimpleGradientFrame(header_content, self.theme_colors['dark']['header_bg'])
        control_frame.pack(side='right')
        
        user_info = tk.Label(control_frame, 
                           text=f"👤 {self.current_user['name']} ({self.current_user['id']})",
                           bg=self.theme_colors['dark']['header_bg'], 
                           fg='white', font=('Arial', 14, 'bold'))
        user_info.pack(pady=5)
        
        # Control buttons
        btn_frame = SimpleGradientFrame(control_frame, self.theme_colors['dark']['header_bg'])
        btn_frame.pack()
        
        theme_btn = ModernButton(btn_frame, text="🌙 Dark" if self.dark_mode else "☀️ Light",
                                command=self.toggle_theme,
                                bg=self.theme_colors['dark']['accent'],
                                font=('Arial', 10, 'bold'), padx=10, pady=5)
        theme_btn.pack(side='left', padx=5)
        
        logout_btn = ModernButton(btn_frame, text="🚪 Logout", command=self.logout,
                                 bg=self.theme_colors['dark']['danger'],
                                 font=('Arial', 10, 'bold'), padx=10, pady=5)
        logout_btn.pack(side='left', padx=5)
        
        # Main content with notebook
        self.create_main_notebook()
    
    def create_main_notebook(self):
        """Create main notebook with styled tabs"""
        notebook = ttk.Notebook(self.root, style='Custom.TNotebook')
        notebook.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Create tabs
        tabs = [
            ("📢 ANNOUNCEMENTS", self.create_announcements_tab),
            ("📚 ASSIGNMENTS", self.create_assignments_tab),
            ("💻 IT LAB BOOKING", self.create_lab_booking_tab),  # Changed tab name
            ("📅 TIMETABLE", self.create_timetable_tab),
            ("📊 GRADES", self.create_grades_tab),
            ("👥 DIRECTORY", self.create_directory_tab)
        ]
        
        for tab_name, tab_method in tabs:
            frame = SimpleGradientFrame(notebook, self.theme_colors['dark']['bg'])
            notebook.add(frame, text=tab_name)
            tab_method(frame)
    
    def create_announcements_tab(self, parent):
        """Create announcements tab"""
        header = self.create_gradient_header(parent, "📢 LATEST ANNOUNCEMENTS 📢", 
                                           self.theme_colors['dark']['header_bg'])
        
        # Content
        content_frame = SimpleGradientFrame(parent, self.theme_colors['dark']['bg'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        self.announcements_text = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD, 
                                                          font=('Arial', 12),
                                                          bg=self.theme_colors['dark']['entry_bg'],
                                                          fg=self.theme_colors['dark']['entry_fg'],
                                                          insertbackground='white')
        self.announcements_text.pack(fill='both', expand=True)
        self.update_announcements_display()
    
    def create_assignments_tab(self, parent):
        """Create assignments tab"""
        header = self.create_gradient_header(parent, "📚 ASSIGNMENT MANAGEMENT 📚", 
                                           self.theme_colors['dark']['header_bg'])
        
        # Dual panel layout
        dual_frame = SimpleGradientFrame(parent, self.theme_colors['dark']['bg'])
        dual_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Left panel - Submission history
        left_frame = SimpleGradientFrame(dual_frame, self.theme_colors['dark']['card_bg'])
        left_frame.pack(side='left', fill='both', expand=True, padx=5, pady=5)
        
        tk.Label(left_frame, text="📜 SUBMISSION HISTORY", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 16, 'bold')).pack(pady=10)
        
        self.submissions_text = scrolledtext.ScrolledText(left_frame, wrap=tk.WORD,
                                                         bg=self.theme_colors['dark']['entry_bg'],
                                                         fg='white', font=('Arial', 11),
                                                         insertbackground='white')
        self.submissions_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Right panel - New submission
        right_frame = SimpleGradientFrame(dual_frame, self.theme_colors['dark']['card_bg'])
        right_frame.pack(side='right', fill='both', expand=True, padx=5, pady=5)
        
        tk.Label(right_frame, text="✏️ NEW SUBMISSION", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Form
        form_frame = SimpleGradientFrame(right_frame, self.theme_colors['dark']['card_bg'])
        form_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        tk.Label(form_frame, text="Assignment Name:", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 12)).pack(anchor='w', pady=5)
        
        self.assignment_name = tk.Entry(form_frame, font=('Arial', 12),
                                       bg=self.theme_colors['dark']['entry_bg'],
                                       fg='white', insertbackground='white')
        self.assignment_name.pack(fill='x', pady=5)
        
        tk.Label(form_frame, text="Filename:", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 12)).pack(anchor='w', pady=5)
        
        self.filename = tk.Entry(form_frame, font=('Arial', 12),
                                bg=self.theme_colors['dark']['entry_bg'],
                                fg='white', insertbackground='white')
        self.filename.pack(fill='x', pady=5)
        
        # Buttons
        btn_frame = SimpleGradientFrame(form_frame, self.theme_colors['dark']['card_bg'])
        btn_frame.pack(fill='x', pady=20)
        
        submit_btn = ModernButton(btn_frame, text="📤 SUBMIT", 
                                 command=self.submit_assignment,
                                 bg=self.theme_colors['dark']['success'])
        submit_btn.pack(side='left', expand=True, padx=5)
        
        undo_btn = ModernButton(btn_frame, text="↩️ UNDO", 
                               command=self.undo_submission,
                               bg=self.theme_colors['dark']['warning'])
        undo_btn.pack(side='right', expand=True, padx=5)
        
        self.update_submissions_display()
    
    def submit_assignment(self):
        """Handle assignment submission"""
        name = self.assignment_name.get().strip()
        filename = self.filename.get().strip()
        
        if not name or not filename:
            messagebox.showerror("Error", "Please fill all fields!")
            return
        
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
        submission = f"{name} - {filename} - {timestamp}"
        self.submission_stack.push(submission)
        
        self.update_submissions_display()
        self.assignment_name.delete(0, tk.END)
        self.filename.delete(0, tk.END)
        
        messagebox.showinfo("Success", "Assignment submitted successfully!")
    
    def undo_submission(self):
        """Undo last submission"""
        if self.submission_stack.is_empty():
            messagebox.showinfo("Info", "No submissions to undo!")
            return
        
        undone = self.submission_stack.pop()
        self.update_submissions_display()
        messagebox.showinfo("Undone", f"Removed: {undone}")
    
    def create_lab_booking_tab(self, parent):
        """Create IT Lab booking tab with IT-specific equipment"""
        header = self.create_gradient_header(parent, "💻 IT LAB EQUIPMENT BOOKING 💻", 
                                           self.theme_colors['dark']['header_bg'])
        
        content_frame = SimpleGradientFrame(parent, self.theme_colors['dark']['bg'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Equipment category selection
        category_frame = SimpleGradientFrame(content_frame, self.theme_colors['dark']['card_bg'])
        category_frame.pack(fill='x', pady=10)
        
        tk.Label(category_frame, text="Select Equipment Category:", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 14)).pack(side='left', padx=20, pady=10)
        
        self.category_var = tk.StringVar()
        category_combo = ttk.Combobox(category_frame, textvariable=self.category_var,
                                     values=list(self.lab_equipment.keys()),
                                     font=('Arial', 12), state='readonly')
        category_combo.pack(side='left', padx=10, pady=10)
        category_combo.current(0)
        category_combo.bind('<<ComboboxSelected>>', lambda e: self.update_equipment_list())
        
        # Equipment selection
        equip_frame = SimpleGradientFrame(content_frame, self.theme_colors['dark']['card_bg'])
        equip_frame.pack(fill='x', pady=10)
        
        tk.Label(equip_frame, text="Select Specific Equipment:", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 14)).pack(side='left', padx=20, pady=10)
        
        self.equipment_var = tk.StringVar()
        self.equipment_combo = ttk.Combobox(equip_frame, textvariable=self.equipment_var,
                                           font=('Arial', 12), state='readonly')
        self.equipment_combo.pack(side='left', padx=10, pady=10)
        self.update_equipment_list()
        
        # Booking duration
        duration_frame = SimpleGradientFrame(content_frame, self.theme_colors['dark']['card_bg'])
        duration_frame.pack(fill='x', pady=10)
        
        tk.Label(duration_frame, text="Booking Duration (hours):", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 14)).pack(side='left', padx=20, pady=10)
        
        self.duration_var = tk.StringVar(value="2")
        duration_spinbox = tk.Spinbox(duration_frame, from_=1, to=8, textvariable=self.duration_var,
                                     font=('Arial', 12), width=10,
                                     bg=self.theme_colors['dark']['entry_bg'],
                                     fg='white', insertbackground='white')
        duration_spinbox.pack(side='left', padx=10, pady=10)
        
        # Waiting list
        list_frame = SimpleGradientFrame(content_frame, self.theme_colors['dark']['card_bg'])
        list_frame.pack(fill='both', expand=True, pady=10)
        
        tk.Label(list_frame, text="📋 CURRENT BOOKING QUEUE", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 16, 'bold')).pack(pady=10)
        
        self.waiting_list_text = scrolledtext.ScrolledText(list_frame, wrap=tk.WORD,
                                                          bg=self.theme_colors['dark']['entry_bg'],
                                                          fg='white', font=('Arial', 11),
                                                          insertbackground='white')
        self.waiting_list_text.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Controls
        control_frame = SimpleGradientFrame(content_frame, self.theme_colors['dark']['bg'])
        control_frame.pack(fill='x', pady=10)
        
        join_btn = ModernButton(control_frame, text="➕ BOOK EQUIPMENT", 
                               command=self.join_waiting_list,
                               bg=self.theme_colors['dark']['success'])
        join_btn.pack(side='left', expand=True, padx=5)
        
        process_btn = ModernButton(control_frame, text="➡️ PROCESS NEXT", 
                                  command=self.process_next_student,
                                  bg=self.theme_colors['dark']['accent'])
        process_btn.pack(side='right', expand=True, padx=5)
        
        self.update_waiting_list_display()
    
    def update_equipment_list(self):
        """Update equipment list based on selected category"""
        category = self.category_var.get()
        if category in self.lab_equipment:
            equipment_list = self.lab_equipment[category]
            self.equipment_combo['values'] = equipment_list
            if equipment_list:
                self.equipment_combo.current(0)
    
    def join_waiting_list(self):
        """Add current user to waiting list for IT equipment"""
        if self.current_user:
            category = self.category_var.get()
            equipment = self.equipment_var.get()
            duration = self.duration_var.get()
            
            if not equipment:
                messagebox.showerror("Error", "Please select equipment!")
                return
            
            timestamp = datetime.now().strftime("%H:%M")
            entry = f"{self.current_user['name']} - {equipment} ({category}) - {duration} hours - Booked at {timestamp}"
            self.lab_queue.enqueue(entry)
            self.update_waiting_list_display()
            messagebox.showinfo("Success", f"Booked {equipment} for {duration} hours!\nYou are #{self.lab_queue.size()} in queue.")
    
    def process_next_student(self):
        """Process next student in queue"""
        if self.lab_queue.is_empty():
            messagebox.showinfo("Info", "Queue is empty!")
            return
        
        student = self.lab_queue.dequeue()
        self.update_waiting_list_display()
        
        # Extract equipment info from the queue entry
        equipment_info = student.split(' - ')[1] if ' - ' in student else student
        messagebox.showinfo("Next Student", f"{student}\n\nEquipment is now available for use!")
    
    def create_timetable_tab(self, parent):
        """Create timetable tab"""
        header = self.create_gradient_header(parent, "📅 WEEKLY TIMETABLE 📅", 
                                           self.theme_colors['dark']['header_bg'])
        
        # Timetable content
        timetable_frame = SimpleGradientFrame(parent, self.theme_colors['dark']['bg'])
        timetable_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Create table
        columns = ['Time'] + self.days
        tree = ttk.Treeview(timetable_frame, columns=columns, show='headings', height=15)
        
        for col in columns:
            tree.heading(col, text=col)
            tree.column(col, width=150)
        
        for row in self.timetable:
            tree.insert('', 'end', values=row)
        
        scrollbar = ttk.Scrollbar(timetable_frame, orient=tk.VERTICAL, command=tree.yview)
        tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        tree.pack(fill='both', expand=True)
    
    def create_grades_tab(self, parent):
        """Create grades tab"""
        header = self.create_gradient_header(parent, "📊 GRADE ANALYSIS 📊", 
                                           self.theme_colors['dark']['header_bg'])
        
        content_frame = SimpleGradientFrame(parent, self.theme_colors['dark']['bg'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Grades display
        grades_text = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD,
                                              font=('Arial', 12),
                                              bg=self.theme_colors['dark']['entry_bg'],
                                              fg='white',
                                              insertbackground='white')
        grades_text.pack(fill='both', expand=True)
        
        # Add grade analysis
        analysis = self.analyze_grades()
        grades_text.insert(tk.END, analysis)
        grades_text.config(state=tk.DISABLED)
    
    def analyze_grades(self):
        """Analyze and format grades"""
        avg = sum(self.grades) / len(self.grades)
        highest = max(self.grades)
        lowest = min(self.grades)
        
        analysis = f"""📊 GRADE ANALYSIS REPORT 📊

Overall Performance:
• Average Grade: {avg:.1f}%
• Highest Grade: {highest}%
• Lowest Grade: {lowest}%

Subject-wise Grades:
"""
        subjects = ['Mathematics', 'Physics', 'Chemistry', 'Biology', 
                   'Computer Science', 'English', 'History', 'Art']
        
        for subject, grade in zip(subjects, self.grades):
            analysis += f"• {subject}: {grade}%\n"
        
        analysis += f"""
Grade Distribution:
• A (90-100): {len([g for g in self.grades if g >= 90])} subjects
• B (80-89): {len([g for g in self.grades if 80 <= g < 90])} subjects  
• C (70-79): {len([g for g in self.grades if 70 <= g < 80])} subjects
• D (60-69): {len([g for g in self.grades if 60 <= g < 70])} subjects
• F (<60): {len([g for g in self.grades if g < 60])} subjects
"""
        return analysis
    
    def create_directory_tab(self, parent):
        """Create student directory tab"""
        header = self.create_gradient_header(parent, "👥 STUDENT DIRECTORY 👥", 
                                           self.theme_colors['dark']['header_bg'])
        
        content_frame = SimpleGradientFrame(parent, self.theme_colors['dark']['bg'])
        content_frame.pack(fill='both', expand=True, padx=20, pady=20)
        
        # Search frame
        search_frame = SimpleGradientFrame(content_frame, self.theme_colors['dark']['card_bg'])
        search_frame.pack(fill='x', pady=10)
        
        tk.Label(search_frame, text="🔍 Search:", 
                bg=self.theme_colors['dark']['card_bg'], 
                fg='white', font=('Arial', 12)).pack(side='left', padx=20, pady=10)
        
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var, font=('Arial', 12),
                               bg=self.theme_colors['dark']['entry_bg'], fg='white',
                               insertbackground='white')
        search_entry.pack(side='left', fill='x', expand=True, padx=10, pady=10)
        search_entry.bind('<KeyRelease>', lambda e: self.search_student())
        
        # Directory display
        self.directory_text = scrolledtext.ScrolledText(content_frame, wrap=tk.WORD,
                                                       font=('Arial', 11),
                                                       bg=self.theme_colors['dark']['entry_bg'],
                                                       fg='white',
                                                       insertbackground='white')
        self.directory_text.pack(fill='both', expand=True)
        self.display_all_students()
    
    def display_all_students(self):
        """Display all students in directory"""
        self.directory_text.config(state=tk.NORMAL)
        self.directory_text.delete(1.0, tk.END)
        
        self.directory_text.insert(tk.END, "🎓 STUDENT DIRECTORY 🎓\n\n")
        for student_id, info in self.students.items():
            self.directory_text.insert(tk.END, 
                f"ID: {student_id}\n"
                f"Name: {info['name']}\n" 
                f"Phone: {info['phone']}\n"
                f"Year: {info['year']} | Department: {info['department']}\n"
                f"{'='*50}\n"
            )
        
        self.directory_text.config(state=tk.DISABLED)
    
    def search_student(self):
        """Search students by name or ID"""
        query = self.search_var.get().lower()
        
        self.directory_text.config(state=tk.NORMAL)
        self.directory_text.delete(1.0, tk.END)
        
        if not query:
            self.display_all_students()
            return
        
        results = []
        for student_id, info in self.students.items():
            if (query in info['name'].lower() or 
                query in student_id.lower() or 
                query in info['department'].lower()):
                results.append((student_id, info))
        
        if results:
            self.directory_text.insert(tk.END, f"🔍 SEARCH RESULTS ({len(results)} found)\n\n")
            for student_id, info in results:
                self.directory_text.insert(tk.END,
                    f"ID: {student_id}\n"
                    f"Name: {info['name']}\n"
                    f"Phone: {info['phone']}\n" 
                    f"Year: {info['year']} | Department: {info['department']}\n"
                    f"{'='*50}\n"
                )
        else:
            self.directory_text.insert(tk.END, "No students found matching your search.")
        
        self.directory_text.config(state=tk.DISABLED)
    
    def add_sample_data(self):
        """Add sample data to the system"""
        self.announcements.add_announcement("2024-12-19 09:00 - Python Practical class moved to Lab 2")
        self.announcements.add_announcement("2024-12-18 15:30 - IT Lab will be closed for maintenance tomorrow")
        self.announcements.add_announcement("2024-12-17 10:00 - New Raspberry Pi kits available in IT Lab")
        
        self.submission_stack.push("Data Structures Assignment - linked_list.cpp - 2024-12-18 14:30")
        self.submission_stack.push("Python Programming - calculator.py - 2024-12-17 16:45")
        
        # Sample IT lab bookings
        self.lab_queue.enqueue("Sachin Singh - High-Performance Desktop (Computer Systems) - 2 hours - Booked at 10:30")
        self.lab_queue.enqueue("Himani Malankar - Cisco Router & Switch Lab Kit (Networking) - 3 hours - Booked at 11:15")
    
    def update_announcements_display(self):
        """Update announcements display"""
        if hasattr(self, 'announcements_text') and self.announcements_text.winfo_exists():
            self.announcements_text.config(state=tk.NORMAL)
            self.announcements_text.delete(1.0, tk.END)
            
            announcements = self.announcements.display_announcements()
            if announcements:
                for announcement in announcements:
                    self.announcements_text.insert(tk.END, announcement + "\n\n")
            else:
                self.announcements_text.insert(tk.END, "No announcements available.")
            
            self.announcements_text.config(state=tk.DISABLED)
    
    def update_submissions_display(self):
        """Update submissions display"""
        if hasattr(self, 'submissions_text') and self.submissions_text.winfo_exists():
            self.submissions_text.config(state=tk.NORMAL)
            self.submissions_text.delete(1.0, tk.END)
            
            submissions = self.submission_stack.display_stack()
            if submissions:
                for submission in submissions:
                    self.submissions_text.insert(tk.END, submission + "\n\n")
            else:
                self.submissions_text.insert(tk.END, "No submissions yet.")
            
            self.submissions_text.config(state=tk.DISABLED)
    
    def update_waiting_list_display(self):
        """Update waiting list display"""
        if hasattr(self, 'waiting_list_text') and self.waiting_list_text.winfo_exists():
            self.waiting_list_text.config(state=tk.NORMAL)
            self.waiting_list_text.delete(1.0, tk.END)
            
            waiting_list = self.lab_queue.display_queue()
            if waiting_list:
                self.waiting_list_text.insert(tk.END, "💻 IT LAB BOOKING QUEUE 💻\n\n")
                for student in waiting_list:
                    self.waiting_list_text.insert(tk.END, student + "\n\n")
            else:
                self.waiting_list_text.insert(tk.END, "No equipment bookings in queue.")
            
            self.waiting_list_text.config(state=tk.DISABLED)
    
    def toggle_theme(self):
        """Toggle between dark and light mode"""
        self.dark_mode = not self.dark_mode
        theme_name = 'light' if not self.dark_mode else 'dark'  # Fixed logic
        messagebox.showinfo("Theme", f"Switched to {theme_name} mode!")
        # Note: Full theme switching would require updating all colors dynamically
    
    def logout(self):
        """Handle logout"""
        if messagebox.askyesno("Logout", "Are you sure you want to logout?"):
            self.current_user = None
            self.create_login_screen()
    
    def clear_screen(self):
        """Clear all widgets from screen"""
        for widget in self.root.winfo_children():
            widget.destroy()

def main():
    root = tk.Tk()
    app = CampusConnectGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
