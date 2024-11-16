import tkinter as tk
from tkinter import ttk
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class STEMLearningPlatform:
    def __init__(self, root):
        self.root = root
        self.root.title("STEM Learning Platform")
        self.root.geometry("1000x600")
        
        # Create main container
        self.main_container = ttk.Frame(self.root)
        self.main_container.pack(expand=True, fill='both', padx=10, pady=10)
        
        # Create navigation sidebar
        self.create_sidebar()
        
        # Create main content area
        self.content_frame = ttk.Frame(self.main_container)
        self.content_frame.pack(side='left', expand=True, fill='both')
        
        # Initialize modules dictionary
        self.modules = {
            'Physics': self.physics_module,
            'Programming': self.programming_module,
            'Mathematics': self.math_module,
            'Engineering': self.engineering_module
        }
        
        # Start with welcome screen
        self.show_welcome_screen()
    
    def create_sidebar(self):
        sidebar = ttk.Frame(self.main_container, style='Sidebar.TFrame')
        sidebar.pack(side='left', fill='y', padx=(0, 10))
        
        # Create module buttons
        ttk.Label(sidebar, text="Learning Modules", font=('Arial', 12, 'bold')).pack(pady=(0, 10))
        
        modules = ['Physics', 'Programming', 'Mathematics', 'Engineering']
        for module in modules:
            ttk.Button(sidebar, text=module, 
                      command=lambda m=module: self.modules[m]()).pack(pady=5, fill='x')
    
    def show_welcome_screen(self):
        self.clear_content()
        welcome_frame = ttk.Frame(self.content_frame)
        welcome_frame.pack(expand=True, fill='both')
        
        ttk.Label(welcome_frame, 
                 text="Welcome to STEM Learning Platform!", 
                 font=('Arial', 20, 'bold')).pack(pady=20)
        
        ttk.Label(welcome_frame, 
                 text="Choose a module from the sidebar to begin your learning journey.",
                 font=('Arial', 12)).pack(pady=10)
    
    def clear_content(self):
        for widget in self.content_frame.winfo_children():
            widget.destroy()
    
    def physics_module(self):
        self.clear_content()
        physics_frame = ttk.Frame(self.content_frame)
        physics_frame.pack(expand=True, fill='both')
        
        ttk.Label(physics_frame, text="Physics Experiments", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Gravity Simulation
        def run_gravity_simulation():
            # Create matplotlib figure
            fig, ax = plt.subplots(figsize=(6, 4))
            t = np.linspace(0, 10, 100)
            h = 100 - 4.9*t**2  # Height equation
            ax.plot(t, h)
            ax.set_title('Object Fall Under Gravity')
            ax.set_xlabel('Time (s)')
            ax.set_ylabel('Height (m)')
            ax.grid(True)
            
            # Embed in tkinter
            canvas = FigureCanvasTkAgg(fig, master=physics_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(pady=10)
        
        ttk.Button(physics_frame, text="Run Gravity Simulation", 
                  command=run_gravity_simulation).pack(pady=5)
    
    def programming_module(self):
        self.clear_content()
        programming_frame = ttk.Frame(self.content_frame)
        programming_frame.pack(expand=True, fill='both')
        
        ttk.Label(programming_frame, text="Learn Programming", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Simple code editor
        code_editor = tk.Text(programming_frame, height=10)
        code_editor.pack(pady=10, fill='x')
        code_editor.insert('1.0', '# Write your Python code here\n')
        
        def run_code():
            code = code_editor.get('1.0', tk.END)
            try:
                exec(code)
            except Exception as e:
                result_label.config(text=f"Error: {str(e)}")
        
        ttk.Button(programming_frame, text="Run Code", 
                  command=run_code).pack(pady=5)
        
        result_label = ttk.Label(programming_frame, text="")
        result_label.pack(pady=5)
    
    def math_module(self):
        self.clear_content()
        math_frame = ttk.Frame(self.content_frame)
        math_frame.pack(expand=True, fill='both')
        
        ttk.Label(math_frame, text="Interactive Mathematics", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Function plotter
        def plot_function():
            try:
                x = np.linspace(-10, 10, 200)
                y = eval(func_entry.get())
                
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.plot(x, y)
                ax.grid(True)
                ax.set_title('Function Plot')
                
                canvas = FigureCanvasTkAgg(fig, master=math_frame)
                canvas.draw()
                canvas.get_tk_widget().pack(pady=10)
            except Exception as e:
                ttk.Label(math_frame, text=f"Error: {str(e)}").pack()
        
        ttk.Label(math_frame, text="Enter a function (use 'x' as variable):").pack()
        func_entry = ttk.Entry(math_frame)
        func_entry.pack(pady=5)
        func_entry.insert(0, "x**2")  # Default function
        
        ttk.Button(math_frame, text="Plot Function", 
                  command=plot_function).pack(pady=5)
    
    def engineering_module(self):
        self.clear_content()
        engineering_frame = ttk.Frame(self.content_frame)
        engineering_frame.pack(expand=True, fill='both')
        
        ttk.Label(engineering_frame, text="Engineering Projects", 
                 font=('Arial', 16, 'bold')).pack(pady=10)
        
        # Bridge simulator
        def simulate_bridge():
            # Simple bridge stress visualization
            fig, ax = plt.subplots(figsize=(6, 4))
            x = np.linspace(0, 10, 100)
            load = float(load_entry.get())
            deflection = load * np.sin(np.pi * x / 10)
            ax.plot(x, deflection)
            ax.set_title('Bridge Deflection Under Load')
            ax.set_xlabel('Position (m)')
            ax.set_ylabel('Deflection (mm)')
            ax.grid(True)
            
            canvas = FigureCanvasTkAgg(fig, master=engineering_frame)
            canvas.draw()
            canvas.get_tk_widget().pack(pady=10)
        
        ttk.Label(engineering_frame, text="Enter bridge load (kN):").pack()
        load_entry = ttk.Entry(engineering_frame)
        load_entry.pack(pady=5)
        load_entry.insert(0, "10")  # Default load
        
        ttk.Button(engineering_frame, text="Simulate Bridge", 
                  command=simulate_bridge).pack(pady=5)

if __name__ == "__main__":
    root = tk.Tk()
    app = STEMLearningPlatform(root)
    root.mainloop()