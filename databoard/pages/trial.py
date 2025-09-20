import reflex as rx
from ..components.navbar import navbar

class TrialState(rx.State):
    """State for trial page and file upload functionality."""
    
    # File upload
    uploaded_files: list[str] = []
    is_uploading: bool = False
    upload_progress: int = 0
    
    # File analysis
    file_analyzed: bool = False
    file_name: str = ""
    file_size: str = ""
    row_count: int = 0
    column_count: int = 0
    
    # Dashboard generation
    dashboard_generated: bool = False
    is_generating: bool = False
    generation_progress: int = 0
    
    # Sample data preview
    sample_columns: list[str] = []
    
    async def handle_upload(self, files: list[str]):
        """Handle file upload and processing."""
        self.is_uploading = True
        self.upload_progress = 0
        
        # Simulate upload progress
        for i in range(1, 101, 10):
            self.upload_progress = i
            await rx.sleep(0.1)
        
        # Process the uploaded file
        if files:
            self.uploaded_files = files
            self.file_name = files[0].split("/")[-1] if "/" in files[0] else files[0]
            self.file_size = "2.3 MB"  # Mock file size
            self.row_count = 15420  # Mock row count
            self.column_count = 12  # Mock column count
            self.sample_columns = [
                "Customer_ID", "Product_Name", "Sales_Amount", 
                "Date", "Region", "Category", "Quantity", 
                "Discount", "Profit", "Customer_Segment"
            ]
            self.file_analyzed = True
        
        self.is_uploading = False
        self.upload_progress = 100
    
    async def generate_dashboard(self):
        """Generate dashboard from uploaded data."""
        self.is_generating = True
        self.generation_progress = 0
        
        # Simulate dashboard generation progress
        steps = [
            ("Analyzing data structure...", 20),
            ("Creating visualizations...", 40), 
            ("Generating insights...", 60),
            ("Building interactive charts...", 80),
            ("Finalizing dashboard...", 100)
        ]
        
        for step, progress in steps:
            self.generation_progress = progress
            await rx.sleep(1)
        
        self.dashboard_generated = True
        self.is_generating = False
    
    def reset_trial(self):
        """Reset trial to initial state."""
        self.uploaded_files = []
        self.file_analyzed = False
        self.dashboard_generated = False
        self.is_uploading = False
        self.is_generating = False
        self.upload_progress = 0
        self.generation_progress = 0
        self.file_name = ""

def upload_section() -> rx.Component:
    """File upload section component."""
    return rx.box(
        rx.vstack(
            # Upload header
            rx.vstack(
                rx.icon(
                    "cloud-upload", 
                    size=48, 
                    color="#3B82F6",
                    style={
                        "animation": "float 3s ease-in-out infinite",
                    }
                ),
                rx.heading(
                    "Upload Your Data",
                    size="6",
                    weight="bold",
                    color="#111827",
                    text_align="center",
                ),
                rx.text(
                    "Drop your CSV or Excel files here to get started",
                    size="3",
                    color="#374151",
                    text_align="center",
                ),
                spacing="3",
                align_items="center",
            ),
            
            # Upload area
            rx.box(
                rx.cond(
                    TrialState.is_uploading,
                    # Upload progress
                    rx.vstack(
                        rx.spinner(size="3"),
                        rx.text(
                            f"Uploading... {TrialState.upload_progress}%",
                            size="3",
                            color="#3B82F6",
                            weight="medium",
                        ),
                        rx.progress(
                            value=TrialState.upload_progress,
                            max=100,
                            width="300px",
                        ),
                        spacing="4",
                        align_items="center",
                    ),
                    # Upload interface
                    rx.vstack(
                        rx.upload(
                            rx.vstack(
                                rx.icon("file-plus", size=32, color="#6b7280"),
                                rx.text(
                                    "Click to browse or drag & drop",
                                    size="3",
                                    color="#6b7280",
                                    weight="medium",
                                ),
                                rx.text(
                                    "Supports .csv, .xlsx, .xls files",
                                    size="2",
                                    color="#9ca3af",
                                ),
                                spacing="3",
                                align_items="center",
                            ),
                            id="upload1",
                            border="2px dashed #d1d5db",
                            padding="3rem 2rem",
                            border_radius="16px",
                            width="100%",
                            max_width="500px",
                            style={
                                "_hover": {
                                    "border_color": "#3B82F6",
                                    "background": "rgba(59, 130, 246, 0.05)",
                                },
                                "transition": "all 0.3s ease",
                                "cursor": "pointer",
                            }
                        ),
                        rx.button(
                            "Process Upload",
                            on_click=lambda: TrialState.handle_upload(rx.upload_files(upload_id="upload1")),
                            size="3",
                            style={
                                "background": "linear-gradient(45deg, #3B82F6, #8B5CF6)",
                                "cursor": "pointer",
                                "_hover": {
                                    "transform": "translateY(-2px)",
                                    "box_shadow": "0 8px 20px rgba(59, 130, 246, 0.3)",
                                }
                            }
                        ),
                        spacing="4",
                        align_items="center",
                    )
                ),
                width="100%",
                align_items="center",
            ),
            
            spacing="6",
            align_items="center",
            padding="3rem 2rem",
        ),
        background="white",
        border_radius="20px",
        box_shadow="0 10px 40px rgba(0,0,0,0.08)",
        width="100%",
        max_width="600px",
    )

def analysis_section() -> rx.Component:
    """Data analysis results component."""
    return rx.box(
        rx.vstack(
            # Analysis header
            rx.hstack(
                rx.icon("bar-chart-3", size=32, color="#22c55e"),
                rx.vstack(
                    rx.heading(
                        "Data Analysis Complete",
                        size="5",
                        weight="bold",
                        color="#111827",
                    ),
                    rx.text(
                        f"File: {TrialState.file_name}",
                        size="2",
                        color="#6b7280",
                    ),
                    spacing="1",
                    align_items="flex-start",
                ),
                spacing="4",
                align_items="center",
                width="100%",
            ),
            
            # Data statistics
            rx.hstack(
                # Rows stat
                rx.vstack(
                    rx.text(
                        f"{TrialState.row_count:,}",
                        size="6",
                        weight="bold",
                        color="#3B82F6",
                    ),
                    rx.text(
                        "Rows",
                        size="2",
                        color="#6b7280",
                        weight="medium",
                    ),
                    spacing="1",
                    align_items="center",
                    padding="1.5rem",
                    background="rgba(59, 130, 246, 0.1)",
                    border_radius="12px",
                ),
                
                # Columns stat
                rx.vstack(
                    rx.text(
                        TrialState.column_count.to_string(),
                        size="6",
                        weight="bold",
                        color="#8B5CF6",
                    ),
                    rx.text(
                        "Columns",
                        size="2",
                        color="#6b7280",
                        weight="medium",
                    ),
                    spacing="1",
                    align_items="center",
                    padding="1.5rem",
                    background="rgba(139, 92, 246, 0.1)",
                    border_radius="12px",
                ),
                
                # File size stat
                rx.vstack(
                    rx.text(
                        TrialState.file_size,
                        size="6",
                        weight="bold",
                        color="#EC4899",
                    ),
                    rx.text(
                        "Size",
                        size="2",
                        color="#6b7280",
                        weight="medium",
                    ),
                    spacing="1",
                    align_items="center",
                    padding="1.5rem",
                    background="rgba(236, 72, 153, 0.1)",
                    border_radius="12px",
                ),
                
                spacing="4",
                justify="center",
                wrap="wrap",
            ),
            
            # Sample columns preview
            rx.vstack(
                rx.text(
                    "Detected Columns",
                    size="3",
                    weight="bold",
                    color="#111827",
                ),
                rx.hstack(
                    rx.foreach(
                        TrialState.sample_columns[:5],  # Show first 5 columns
                        lambda col: rx.badge(
                            col,
                            variant="soft",
                            color_scheme="blue",
                            size="2",
                        )
                    ),
                    rx.cond(
                        TrialState.sample_columns.length() > 5,
                        rx.badge(
                            f"+{TrialState.sample_columns.length() - 5} more",
                            variant="outline",
                            size="2",
                        )
                    ),
                    spacing="2",
                    wrap="wrap",
                    justify="center",
                ),
                spacing="3",
                align_items="center",
            ),
            
            # Generate dashboard button
            rx.button(
                rx.hstack(
                    rx.icon("zap", size=18),
                    rx.text("Generate Dashboard"),
                    spacing="2"
                ),
                size="3",
                on_click=TrialState.generate_dashboard,
                style={
                    "background": "linear-gradient(45deg, #22c55e, #3B82F6)",
                    "cursor": "pointer",
                    "_hover": {
                        "transform": "translateY(-2px)",
                        "box_shadow": "0 8px 20px rgba(34, 197, 94, 0.3)",
                    }
                }
            ),
            
            spacing="6",
            align_items="center",
            padding="2rem",
        ),
        background="white",
        border_radius="20px",
        box_shadow="0 10px 40px rgba(0,0,0,0.08)",
        width="100%",
        max_width="600px",
        style={
            "animation": "slideIn 0.5s ease-out",
        }
    )

def dashboard_generation() -> rx.Component:
    """Dashboard generation progress component."""
    return rx.box(
        rx.vstack(
            rx.icon(
                "settings",
                size=48,
                color="#3B82F6",
                style={
                    "animation": "spin 2s linear infinite",
                }
            ),
            rx.heading(
                "Generating Your Dashboard",
                size="5",
                weight="bold",
                color="#111827",
                text_align="center",
            ),
            rx.text(
                "Please wait while we create your personalized analytics dashboard",
                size="3",
                color="#6b7280",
                text_align="center",
            ),
            rx.progress(
                value=TrialState.generation_progress,
                max=100,
                width="400px",
            ),
            rx.text(
                f"{TrialState.generation_progress}% Complete",
                size="2",
                color="#3B82F6",
                weight="medium",
            ),
            spacing="4",
            align_items="center",
            padding="3rem 2rem",
        ),
        background="white",
        border_radius="20px",
        box_shadow="0 10px 40px rgba(0,0,0,0.08)",
        width="100%",
        max_width="500px",
    )

def dashboard_ready() -> rx.Component:
    """Dashboard ready component."""
    return rx.box(
        rx.vstack(
            rx.icon(
                "check-circle",
                size=64,
                color="#22c55e",
                style={
                    "animation": "bounce 1s ease-in-out",
                }
            ),
            rx.heading(
                "Dashboard Ready!",
                size="6",
                weight="bold",
                color="#111827",
                text_align="center",
            ),
            rx.text(
                "Your interactive dashboard has been generated successfully",
                size="3",
                color="#6b7280",
                text_align="center",
            ),
            
            # Action buttons
            rx.hstack(
                rx.button(
                    rx.hstack(
                        rx.icon("external-link", size=18),
                        rx.text("View Dashboard"),
                        spacing="2"
                    ),
                    size="3",
                    style={
                        "background": "linear-gradient(45deg, #22c55e, #3B82F6)",
                        "cursor": "pointer",
                        "_hover": {
                            "transform": "translateY(-2px)",
                            "box_shadow": "0 8px 20px rgba(34, 197, 94, 0.3)",
                        }
                    }
                ),
                rx.button(
                    rx.hstack(
                        rx.icon("download", size=18),
                        rx.text("Export"),
                        spacing="2"
                    ),
                    size="3",
                    variant="outline",
                    color="#8B5CF6",
                    border_color="#8B5CF6",
                    style={
                        "cursor": "pointer",
                        "_hover": {
                            "transform": "translateY(-2px)",
                            "background": "rgba(139, 92, 246, 0.1)",
                        }
                    }
                ),
                spacing="4",
            ),
            
            # Try another file
            rx.text(
                "Want to try another file?",
                size="2",
                color="#6b7280",
                margin_top="2rem",
            ),
            rx.button(
                "Upload New File",
                on_click=TrialState.reset_trial,
                variant="ghost",
                size="2",
                color="#3B82F6",
            ),
            
            spacing="4",
            align_items="center",
            padding="3rem 2rem",
        ),
        background="white",
        border_radius="20px",
        box_shadow="0 10px 40px rgba(0,0,0,0.08)",
        width="100%",
        max_width="500px",
        style={
            "animation": "slideIn 0.5s ease-out",
        }
    )

@rx.page(route="/trial", title="Try DataBoard - Free Trial")
def trial() -> rx.Component:
    return rx.vstack(
        navbar("trial"),
        
        # Main content area
        rx.box(
            rx.box(
                rx.vstack(
                    # Page header
                    rx.vstack(
                        rx.heading(
                            "Try DataBoard Free",
                            size="8",
                            weight="bold",
                            background="linear-gradient(45deg, #3B82F6, #8B5CF6, #EC4899)",
                            background_clip="text",
                            color="transparent",
                            text_align="center",
                            style={
                                "animation": "fadeInUp 1s ease-out",
                            }
                        ),
                        rx.text(
                            "Upload your data and see the magic happen in real-time",
                            size="4",
                            color="#374151",
                            text_align="center",
                            max_width="600px",
                            line_height="1.6",
                        ),
                        rx.text(
                            "No signup required • Secure processing • Instant results",
                            size="2",
                            color="#6b7280",
                            text_align="center",
                        ),
                        spacing="4",
                        align_items="center",
                        padding="3rem 2rem 2rem 2rem",
                    ),
                    
                    # Dynamic content based on state
                    rx.cond(
                        TrialState.dashboard_generated,
                        dashboard_ready(),
                        rx.cond(
                            TrialState.is_generating,
                            dashboard_generation(),
                            rx.cond(
                                TrialState.file_analyzed,
                                analysis_section(),
                                upload_section()
                            )
                        )
                    ),
                    
                    spacing="4",
                    align_items="center",
                    width="100%",
                ),
                max_width="1200px",
                margin="0 auto",
                width="100%",
            ),
            
            # Full-width background matching other sections
            background="linear-gradient(135deg, #ffffff 0%, #f8fafc 100%)",
            width="100vw",
            min_height="80vh",
            padding="0 2rem",
            
            # Custom CSS animations
            style={
                "@keyframes fadeInUp": {
                    "from": {
                        "opacity": "0",
                        "transform": "translateY(30px)",
                    },
                    "to": {
                        "opacity": "1",
                        "transform": "translateY(0)",
                    },
                },
                "@keyframes slideIn": {
                    "from": {
                        "opacity": "0",
                        "transform": "scale(0.95)",
                    },
                    "to": {
                        "opacity": "1",
                        "transform": "scale(1)",
                    },
                },
                "@keyframes float": {
                    "0%, 100%": {
                        "transform": "translateY(0px)",
                    },
                    "50%": {
                        "transform": "translateY(-10px)",
                    },
                },
                "@keyframes spin": {
                    "from": {
                        "transform": "rotate(0deg)",
                    },
                    "to": {
                        "transform": "rotate(360deg)",
                    },
                },
                "@keyframes bounce": {
                    "0%, 20%, 53%, 80%, 100%": {
                        "transform": "translateY(0)",
                    },
                    "40%, 43%": {
                        "transform": "translateY(-10px)",
                    },
                    "70%": {
                        "transform": "translateY(-5px)",
                    },
                },
            },
        ),
        
        width="100%",
        spacing="0",
    )