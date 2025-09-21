import reflex as rx

class ContactState(rx.State):
    """State for contact form and interactions."""
    
    # Form fields
    name: str = ""
    email: str = ""
    subject: str = ""
    message: str = ""
    
    # Form status
    is_submitting: bool = False
    form_submitted: bool = False
    show_success: bool = False
    
    # Validation
    name_error: str = ""
    email_error: str = ""
    message_error: str = ""
    
    def set_name(self, value: str):
        self.name = value
        self.name_error = ""
    
    def set_email(self, value: str):
        self.email = value
        self.email_error = ""
    
    def set_subject(self, value: str):
        self.subject = value
    
    def set_message(self, value: str):
        self.message = value
        self.message_error = ""
    
    def validate_form(self) -> bool:
        """Validate form fields."""
        is_valid = True
        
        if not self.name.strip():
            self.name_error = "Name is required"
            is_valid = False
        
        if not self.email.strip():
            self.email_error = "Email is required"
            is_valid = False
        elif "@" not in self.email:
            self.email_error = "Please enter a valid email"
            is_valid = False
        
        if not self.message.strip():
            self.message_error = "Message is required"
            is_valid = False
        
        return is_valid
    
    async def submit_form(self):
        """Handle form submission."""
        if not self.validate_form():
            return
        
        self.is_submitting = True
        
        # Simulate API call
        await rx.sleep(2)
        
        # Reset form and show success
        self.name = ""
        self.email = ""
        self.subject = ""
        self.message = ""
        self.is_submitting = False
        self.form_submitted = True
        self.show_success = True
        
        # Hide success message after 5 seconds
        await rx.sleep(5)
        self.show_success = False

def contact_info_card(icon: str, title: str, info: str, subinfo: str = "") -> rx.Component:
    """Contact information card component."""
    return rx.vstack(
        rx.box(
            rx.icon(icon, size=32, color="#3B82F6"),
            padding="1rem",
            border_radius="50%",
            background="rgba(59, 130, 246, 0.1)",
            style={
                "animation": "float 3s ease-in-out infinite",
            }
        ),
        rx.text(
            title,
            size="3",
            weight="bold",
            color="#111827",
            text_align="center",
        ),
        rx.text(
            info,
            size="2",
            color="#374151",
            text_align="center",
            weight="medium",
        ),
        rx.cond(
            subinfo != "",
            rx.text(
                subinfo,
                size="1",
                color="#6b7280",
                text_align="center",
            )
        ),
        spacing="3",
        align_items="center",
        padding="2rem",
        background="white",
        border_radius="16px",
        box_shadow="0 4px 20px rgba(0,0,0,0.08)",
        style={
            "animation": "fadeInUp 1s ease-out",
            "_hover": {
                "transform": "translateY(-4px)",
                "box_shadow": "0 8px 30px rgba(0,0,0,0.12)",
            },
            "transition": "all 0.3s ease",
        }
    )

def contact() -> rx.Component:
    return rx.box(
        # Content wrapper with max width
        rx.box(
            rx.vstack(
                # Section header
                rx.vstack(
                    rx.heading(
                        "Get In Touch",
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
                        "Have questions about DataBoard? We'd love to hear from you.",
                        size="4",
                        color="#374151",
                        text_align="center",
                        max_width="600px",
                        line_height="1.6",
                    ),
                    rx.text(
                        "Send us a message and we'll respond as soon as possible.",
                        size="3",
                        color="#6b7280",
                        text_align="center",
                        max_width="500px",
                        line_height="1.5",
                    ),
                    spacing="4",
                    align_items="center",
                    padding="3rem 2rem 2rem 2rem",
                ),
                
                # Contact info cards
                rx.hstack(
                    contact_info_card(
                        "mail",
                        "Email Us",
                        "support@databoard.com",
                        "We'll respond within 24 hours"
                    ),
                    contact_info_card(
                        "phone",
                        "Call Us", 
                        "+1 (555) 123-4567",
                        "Mon-Fri, 9AM-6PM EST"
                    ),
                    contact_info_card(
                        "map-pin",
                        "Visit Us",
                        "123 Data Street",
                        "San Francisco, CA 94102"
                    ),
                    spacing="6",
                    justify="center",
                    wrap="wrap",
                    margin_bottom="3rem",
                ),
                
                # Contact form section
                rx.box(
                    # Success message
                    rx.cond(
                        ContactState.show_success,
                        rx.box(
                            rx.hstack(
                                rx.icon("check-circle-2", size=20, color="#22c55e"),
                                rx.text(
                                    "Message sent successfully! We'll get back to you soon.",
                                    size="3",
                                    color="#22c55e",
                                    weight="medium",
                                ),
                                spacing="3",
                                align_items="center",
                            ),
                            padding="1rem 1.5rem",
                            background="rgba(34, 197, 94, 0.1)",
                            border="1px solid rgba(34, 197, 94, 0.3)",
                            border_radius="12px",
                            margin_bottom="2rem",
                            style={
                                "animation": "slideIn 0.5s ease-out",
                            }
                        )
                    ),
                    
                    rx.vstack(
                        rx.heading(
                            "Send us a Message",
                            size="6",
                            weight="bold",
                            color="#111827",
                            text_align="center",
                            margin_bottom="2rem",
                        ),
                        
                        # Form fields
                        rx.hstack(
                            # Name field
                            rx.vstack(
                                rx.text("Name *", size="2", weight="medium", color="#374151"),
                                rx.input(
                                    placeholder="Your full name",
                                    value=ContactState.name,
                                    on_change=ContactState.set_name,
                                    size="3",
                                    width="100%",
                                    style={
                                        "border_color": rx.cond(
                                            ContactState.name_error != "",
                                            "#ef4444",
                                            "#d1d5db"
                                        ),
                                    }
                                ),
                                rx.cond(
                                    ContactState.name_error != "",
                                    rx.text(
                                        ContactState.name_error,
                                        size="1",
                                        color="#ef4444",
                                    )
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            
                            # Email field  
                            rx.vstack(
                                rx.text("Email *", size="2", weight="medium", color="#374151"),
                                rx.input(
                                    placeholder="your@email.com",
                                    type="email",
                                    value=ContactState.email,
                                    on_change=ContactState.set_email,
                                    size="3",
                                    width="100%",
                                    style={
                                        "border_color": rx.cond(
                                            ContactState.email_error != "",
                                            "#ef4444",
                                            "#d1d5db"
                                        ),
                                    }
                                ),
                                rx.cond(
                                    ContactState.email_error != "",
                                    rx.text(
                                        ContactState.email_error,
                                        size="1",
                                        color="#ef4444",
                                    )
                                ),
                                spacing="2",
                                width="100%",
                            ),
                            
                            spacing="4",
                            width="100%",
                        ),
                        
                        # Subject field
                        rx.vstack(
                            rx.text("Subject", size="2", weight="medium", color="#374151"),
                            rx.input(
                                placeholder="What's this about?",
                                value=ContactState.subject,
                                on_change=ContactState.set_subject,
                                size="3",
                                width="100%",
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        
                        # Message field
                        rx.vstack(
                            rx.text("Message *", size="2", weight="medium", color="#374151"),
                            rx.text_area(
                                placeholder="Tell us how we can help you...",
                                value=ContactState.message,
                                on_change=ContactState.set_message,
                                min_height="120px",
                                resize="vertical",
                                style={
                                    "border_color": rx.cond(
                                        ContactState.message_error != "",
                                        "#ef4444",
                                        "#d1d5db"
                                    ),
                                }
                            ),
                            rx.cond(
                                ContactState.message_error != "",
                                rx.text(
                                    ContactState.message_error,
                                    size="1",
                                    color="#ef4444",
                                )
                            ),
                            spacing="2",
                            width="100%",
                        ),
                        
                        # Submit button
                        rx.button(
                            rx.cond(
                                ContactState.is_submitting,
                                rx.hstack(
                                    rx.spinner(size="2"),
                                    rx.text("Sending..."),
                                    spacing="2"
                                ),
                                rx.hstack(
                                    rx.icon("send", size=18),
                                    rx.text("Send Message"),
                                    spacing="2"
                                )
                            ),
                            size="3",
                            width="200px",
                            disabled=ContactState.is_submitting,
                            style={
                                "background": "linear-gradient(45deg, #3B82F6, #8B5CF6)",
                                "cursor": rx.cond(ContactState.is_submitting, "not-allowed", "pointer"),
                                "opacity": rx.cond(ContactState.is_submitting, "0.7", "1"),
                                "transform": "translateY(0)",
                                "_hover": {
                                    "transform": "translateY(-2px)",
                                    "box_shadow": "0 10px 25px rgba(59, 130, 246, 0.3)",
                                }
                            },
                            on_click=ContactState.submit_form,
                        ),
                        
                        spacing="6",
                        width="100%",
                        max_width="600px",
                        align_items="center",
                    ),
                    
                    padding="3rem 2rem",
                    background="white",
                    border_radius="20px",
                    box_shadow="0 10px 40px rgba(0,0,0,0.08)",
                    margin="2rem 0",
                    width="100%",
                    max_width="800px",
                ),
                
                # Additional contact methods
                # rx.vstack(
                #     rx.text(
                #         "Prefer other ways to connect?",
                #         size="3",
                #         color="#6b7280",
                #         text_align="center",
                #     ),
                #     rx.hstack(
                #         rx.link(
                #             rx.button(
                #                 rx.hstack(
                #                     rx.icon("message-circle", size=16),
                #                     rx.text("Live Chat"),
                #                     spacing="2"
                #                 ),
                #                 variant="outline",
                #                 size="2",
                #                 color="#3B82F6",
                #                 border_color="#3B82F6",
                #                 style={
                #                     "_hover": {
                #                         "background": "rgba(59, 130, 246, 0.1)",
                #                     }
                #                 }
                #             ),
                #             href="#"
                #         ),
                        # rx.link(
                        #     rx.button(
                        #         rx.hstack(
                        #             rx.icon("book", size=16),
                        #             rx.text("Documentation"),
                        #             spacing="2"
                        #         ),
                        #         variant="outline",
                        #         size="2",
                        #         color="#8B5CF6",
                        #         border_color="#8B5CF6",
                        #         style={
                        #             "_hover": {
                        #                 "background": "rgba(139, 92, 246, 0.1)",
                        #             }
                        #         }
                        #     ),
                        #     href="#"
                        # ),
                    #     rx.link(
                    #         rx.button(
                    #             rx.hstack(
                    #                 rx.icon("circle-help", size=16),
                    #                 rx.text("FAQ"),
                    #                 spacing="2"
                    #             ),
                    #             variant="outline",
                    #             size="2",
                    #             color="#EC4899",
                    #             border_color="#EC4899",
                    #             style={
                    #                 "_hover": {
                    #                     "background": "rgba(236, 72, 153, 0.1)",
                    #                 }
                    #             }
                    #         ),
                    #         href="#"
                    #     ),
                    #     spacing="4",
                    #     wrap="wrap",
                    #     justify="center",
                    # ),
                #     spacing="4",
                #     align_items="center",
                #     padding="2rem",
                # ),
                
                spacing="0",
                width="100%",
                align_items="center",
            ),
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        
        # Full-width background matching header and gallery
        background="linear-gradient(135deg, #ffffff 0%, #f8fafc 100%)",
        width="100vw",
        min_height="80vh",
        
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
        },
        
        id="contact-section"
    )