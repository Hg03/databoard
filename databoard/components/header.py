import reflex as rx

class HeaderState(rx.State):
    """State for header animations and content."""
    
    # Animated descriptions that cycle through
    descriptions: list[str] = [
        "Your AI-powered data exploration assistant.",
        "Transform raw data into actionable insights.",
        "Visualize, analyze, and discover patterns instantly.",
        "Making data science accessible to everyone."
    ]
    
    current_description_index: int = 0
    
    def cycle_description(self):
        """Cycle through different descriptions."""
        self.current_description_index = (self.current_description_index + 1) % len(self.descriptions)
    
    @rx.var
    def current_description(self) -> str:
        return self.descriptions[self.current_description_index]

def header() -> rx.Component:
    return rx.box(
        # Content wrapper with max width for readability
        rx.box(
            rx.vstack(
                # Hero Section
                rx.vstack(
                    # Main heading with gradient text
                    rx.heading(
                        "DataBoard",
                        size="9",
                        weight="bold",
                        background="linear-gradient(45deg, #3B82F6, #8B5CF6, #EC4899)",
                        background_clip="text",
                        color="transparent",
                        text_align="center",
                        style={
                            "animation": "fadeInUp 1s ease-out",
                        }
                    ),
                    
                    # Animated subtitle
                    rx.text(
                        "The Future of Data Analysis",
                        size="5",
                        color="#1e293b",
                        text_align="center",
                        weight="medium",
                        style={
                            "animation": "fadeInUp 1s ease-out 0.2s both",
                        }
                    ),
                    
                    # Animated description that cycles
                    rx.text(
                        HeaderState.current_description,
                        size="4",
                        color="#374151",
                        text_align="center",
                        max_width="600px",
                        line_height="1.6",
                        style={
                            "animation": "textGlow 2s ease-in-out infinite alternate",
                            "transition": "all 0.5s ease-in-out",
                        }
                    ),
                    
                    # Call-to-action buttons
                    rx.hstack(
                        rx.link(
                            rx.button(
                                rx.hstack(
                                    rx.icon("play", size=18),
                                    rx.text("Get Started"),
                                    spacing="2"
                                ),
                                size="3",
                                variant="solid",
                                style={
                                    "background": "linear-gradient(45deg, #3B82F6, #8B5CF6)",
                                    "animation": "fadeInUp 1s ease-out 0.4s both, pulse 2s infinite",
                                    "cursor": "pointer",
                                    "transform": "translateY(0)",
                                    "_hover": {
                                        "transform": "translateY(-2px)",
                                        "box_shadow": "0 10px 25px rgba(59, 130, 246, 0.3)",
                                    }
                                },
                            ),
                            href="/trial"
                        ),
                        rx.button(
                            rx.hstack(
                                rx.icon("book-open", size=18),
                                rx.text("Learn More"),
                                spacing="2"
                            ),
                            size="3",
                            variant="outline",
                            style={
                                "animation": "fadeInUp 1s ease-out 0.6s both",
                                "cursor": "pointer",
                                "transform": "translateY(0)",
                                "_hover": {
                                    "transform": "translateY(-2px)",
                                    "border_color": "#8B5CF6",
                                }
                            }
                        ),
                        spacing="4",
                        style={
                            "margin_top": "2rem",
                        }
                    ),
                    
                    spacing="6",
                    align_items="center",
                    padding="4rem 2rem",
                ),
                
                # Feature highlights with icons
                rx.hstack(
                    # Feature 1
                    rx.vstack(
                        rx.box(
                            rx.icon("bar-chart-3", size=32, color="#3B82F6"),
                            padding="1rem",
                            border_radius="50%",
                            background="rgba(59, 130, 246, 0.1)",
                            style={
                                "animation": "float 3s ease-in-out infinite",
                            }
                        ),
                        rx.text(
                            "Smart Analytics",
                            size="3",
                            weight="bold",
                            color="#111827"
                        ),
                        rx.text(
                            "AI-powered insights",
                            size="2",
                            color="#374151",
                            text_align="center"
                        ),
                        spacing="2",
                        align_items="center",
                        style={
                            "animation": "fadeInUp 1s ease-out 0.8s both",
                        }
                    ),
                    
                    # Feature 2
                    rx.vstack(
                        rx.box(
                            rx.icon("zap", size=32, color="#8B5CF6"),
                            padding="1rem",
                            border_radius="50%",
                            background="rgba(139, 92, 246, 0.1)",
                            style={
                                "animation": "float 3s ease-in-out infinite 0.5s",
                            }
                        ),
                        rx.text(
                            "Lightning Fast",
                            size="3",
                            weight="bold",
                            color="#111827"
                        ),
                        rx.text(
                            "Real-time processing",
                            size="2",
                            color="#374151",
                            text_align="center"
                        ),
                        spacing="2",
                        align_items="center",
                        style={
                            "animation": "fadeInUp 1s ease-out 1s both",
                        }
                    ),
                    
                    # Feature 3
                    rx.vstack(
                        rx.box(
                            rx.icon("shield-check", size=32, color="#EC4899"),
                            padding="1rem",
                            border_radius="50%",
                            background="rgba(236, 72, 153, 0.1)",
                            style={
                                "animation": "float 3s ease-in-out infinite 1s",
                            }
                        ),
                        rx.text(
                            "Secure & Reliable",
                            size="3",
                            weight="bold",
                            color="#111827"
                        ),
                        rx.text(
                            "Enterprise-grade security",
                            size="2",
                            color="#374151",
                            text_align="center"
                        ),
                        spacing="2",
                        align_items="center",
                        style={
                            "animation": "fadeInUp 1s ease-out 1.2s both",
                        }
                    ),
                    
                    spacing="8",
                    justify="center",
                    wrap="wrap",
                    padding="2rem 1rem",
                ),
                
                spacing="0",
                width="100%",
                align_items="center",
            ),
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        
        # Full-width white background with gradient
        background="linear-gradient(135deg, #ffffff 0%, #f8fafc 100%)",
        width="100vw",  # Use viewport width to ensure full width
        min_height="80vh",
        
        # Add custom CSS animations
        style={
            # Keyframe animations
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
            "@keyframes textGlow": {
                "0%": {
                    "color": "rgb(107, 114, 128)",
                },
                "100%": {
                    "color": "rgb(79, 70, 229)",
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
            "@keyframes pulse": {
                "0%": {
                    "box_shadow": "0 0 0 0 rgba(59, 130, 246, 0.7)",
                },
                "70%": {
                    "box_shadow": "0 0 0 10px rgba(59, 130, 246, 0)",
                },
                "100%": {
                    "box_shadow": "0 0 0 0 rgba(59, 130, 246, 0)",
                },
            },
        },
        
        id="header-section"
    )