import reflex as rx

class GalleryState(rx.State):
    """State for gallery image slider."""
    
    # Sample gallery images with descriptions
    gallery_items: list[dict] = [
        {
            "image": "https://picsum.photos/800/400?random=1",
            "title": "Sales Dashboard",
            "description": "Interactive sales analytics with real-time KPIs and trend analysis",
            "category": "Analytics"
        },
        {
            "image": "https://picsum.photos/800/400?random=2", 
            "title": "Customer Insights",
            "description": "Deep dive into customer behavior patterns and segmentation",
            "category": "Customer Data"
        },
        {
            "image": "https://picsum.photos/800/400?random=3",
            "title": "Financial Reports",
            "description": "Comprehensive financial tracking with automated reporting",
            "category": "Finance"
        },
        {
            "image": "https://picsum.photos/800/400?random=4",
            "title": "Inventory Management",
            "description": "Smart inventory tracking with predictive restocking alerts",
            "category": "Operations"
        },
        {
            "image": "https://picsum.photos/800/400?random=5",
            "title": "Marketing Performance",
            "description": "Campaign effectiveness analysis with ROI optimization",
            "category": "Marketing"
        }
    ]
    
    current_index: int = 0
    is_auto_play: bool = True
    
    def next_slide(self):
        """Go to next slide."""
        self.current_index = (self.current_index + 1) % len(self.gallery_items)
    
    def prev_slide(self):
        """Go to previous slide."""
        self.current_index = (self.current_index - 1) % len(self.gallery_items)
    
    def go_to_slide(self, index: int):
        """Go to specific slide."""
        self.current_index = index
    
    def toggle_autoplay(self):
        """Toggle autoplay on/off."""
        self.is_auto_play = not self.is_auto_play
    
    @rx.var
    def current_item(self) -> dict:
        return self.gallery_items[self.current_index]
    
    @rx.var
    def prev_index(self) -> int:
        return (self.current_index - 1) % len(self.gallery_items)
    
    @rx.var 
    def next_index(self) -> int:
        return (self.current_index + 1) % len(self.gallery_items)

def thumbnail_card(item: dict, index: int) -> rx.Component:
    """Small thumbnail card for navigation."""
    return rx.box(
        rx.image(
            src=item["image"],
            width="100%",
            height="60px",
            object_fit="cover",
            border_radius="8px",
        ),
        rx.text(
            item["title"],
            size="1",
            weight="medium",
            color=rx.cond(
                GalleryState.current_index == index,
                "#111827",
                "#6b7280"
            ),
            text_align="center",
            margin_top="0.5rem",
        ),
        width="100px",
        cursor="pointer",
        padding="0.5rem",
        border_radius="12px",
        background=rx.cond(
            GalleryState.current_index == index,
            "white",
            "transparent"
        ),
        box_shadow=rx.cond(
            GalleryState.current_index == index,
            "0 4px 12px rgba(0,0,0,0.1)",
            "none"
        ),
        transform=rx.cond(
            GalleryState.current_index == index,
            "scale(1.05)",
            "scale(1)"
        ),
        transition="all 0.3s ease",
        on_click=lambda: GalleryState.go_to_slide(index),
        style={
            "_hover": {
                "transform": "scale(1.02)",
                "background": "rgba(255,255,255,0.8)",
            }
        }
    )

def gallery() -> rx.Component:
    return rx.box(
        # Content wrapper with max width
        rx.box(
            rx.vstack(
                # Section header
                rx.vstack(
                    rx.heading(
                        "Gallery",
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
                        "Explore stunning data visualizations and dashboard examples",
                        size="4",
                        color="#374151",
                        text_align="center",
                        max_width="600px",
                        line_height="1.6",
                    ),
                    spacing="4",
                    align_items="center",
                    padding="3rem 2rem 2rem 2rem",
                ),
                
                # Main slider section
                rx.vstack(
                    # Main image display
                    rx.box(
                        rx.image(
                            src=GalleryState.current_item["image"],
                            width="100%",
                            height="400px",
                            object_fit="cover",
                            border_radius="16px",
                            style={
                                "animation": "slideIn 0.5s ease-out",
                            }
                        ),
                        
                        # Image overlay with info
                        rx.box(
                            rx.vstack(
                                rx.badge(
                                    GalleryState.current_item["category"],
                                    variant="solid",
                                    color_scheme="blue",
                                    size="2",
                                ),
                                rx.heading(
                                    GalleryState.current_item["title"],
                                    size="6",
                                    weight="bold",
                                    color="white",
                                    text_shadow="2px 2px 4px rgba(0,0,0,0.8)",
                                ),
                                rx.text(
                                    GalleryState.current_item["description"],
                                    size="3",
                                    color="rgba(255,255,255,0.9)",
                                    text_align="center",
                                    max_width="400px",
                                    text_shadow="1px 1px 2px rgba(0,0,0,0.8)",
                                ),
                                spacing="3",
                                align_items="center",
                            ),
                            position="absolute",
                            bottom="0",
                            left="0",
                            right="0",
                            background="linear-gradient(transparent, rgba(0,0,0,0.7))",
                            padding="3rem 2rem 2rem 2rem",
                            border_radius="0 0 16px 16px",
                        ),
                        
                        # Navigation arrows
                        rx.button(
                            rx.icon("chevron-left", size=24),
                            position="absolute",
                            left="1rem",
                            top="50%",
                            transform="translateY(-50%)",
                            background="rgba(255,255,255,0.9)",
                            color="#111827",
                            border_radius="50%",
                            width="48px",
                            height="48px",
                            cursor="pointer",
                            style={
                                "_hover": {
                                    "background": "rgba(255,255,255,1)",
                                    "transform": "translateY(-50%) scale(1.1)",
                                }
                            },
                            on_click=GalleryState.prev_slide,
                        ),
                        rx.button(
                            rx.icon("chevron-right", size=24),
                            position="absolute",
                            right="1rem", 
                            top="50%",
                            transform="translateY(-50%)",
                            background="rgba(255,255,255,0.9)",
                            color="#111827",
                            border_radius="50%",
                            width="48px",
                            height="48px",
                            cursor="pointer",
                            style={
                                "_hover": {
                                    "background": "rgba(255,255,255,1)",
                                    "transform": "translateY(-50%) scale(1.1)",
                                }
                            },
                            on_click=GalleryState.next_slide,
                        ),
                        
                        position="relative",
                        width="100%",
                        max_width="800px",
                    ),
                    
                    # Slide indicators
                    rx.hstack(
                        rx.foreach(
                            GalleryState.gallery_items,
                            lambda item, index: rx.box(
                                width="12px",
                                height="12px", 
                                border_radius="50%",
                                background=rx.cond(
                                    GalleryState.current_index == index,
                                    "#3B82F6",
                                    "rgba(107, 114, 128, 0.4)"
                                ),
                                cursor="pointer",
                                transition="all 0.3s ease",
                                style={
                                    "_hover": {
                                        "transform": "scale(1.2)",
                                    }
                                },
                                on_click=lambda: GalleryState.go_to_slide(index),
                            )
                        ),
                        spacing="3",
                        justify="center",
                        margin_top="1.5rem",
                    ),
                    
                    spacing="4",
                    align_items="center",
                    width="100%",
                ),
                
                # Thumbnail navigation
                rx.vstack(
                    rx.text(
                        "Browse Collection",
                        size="4",
                        weight="bold",
                        color="#111827",
                        text_align="center",
                    ),
                    rx.hstack(
                        rx.foreach(
                            GalleryState.gallery_items,
                            lambda item, index: thumbnail_card(item, index)
                        ),
                        spacing="4",
                        justify="center",
                        wrap="wrap",
                        max_width="600px",
                    ),
                    spacing="4",
                    align_items="center",
                    padding="3rem 2rem",
                ),
                
                # Action buttons
                # rx.hstack(
                #     rx.button(
                #         rx.hstack(
                #             rx.icon("eye", size=18),
                #             rx.text("View All"),
                #             spacing="2"
                #         ),
                #         size="3",
                #         variant="solid",
                #         style={
                #             "background": "linear-gradient(45deg, #3B82F6, #8B5CF6)",
                #             "cursor": "pointer",
                #             "transform": "translateY(0)",
                #             "_hover": {
                #                 "transform": "translateY(-2px)",
                #                 "box_shadow": "0 10px 25px rgba(59, 130, 246, 0.3)",
                #             }
                #         }
                #     ),
                #     rx.button(
                #         rx.hstack(
                #             rx.icon("download", size=18),
                #             rx.text("Download Examples"),
                #             spacing="2"
                #         ),
                #         size="3",
                #         variant="outline",
                #         color="#8B5CF6",
                #         border_color="#8B5CF6",
                #         style={
                #             "cursor": "pointer",
                #             "transform": "translateY(0)",
                #             "_hover": {
                #                 "transform": "translateY(-2px)",
                #                 "background": "rgba(139, 92, 246, 0.1)",
                #             }
                #         }
                #     ),
                #     spacing="4",
                #     margin_bottom="2rem",
                # ),
                
                spacing="0",
                width="100%",
                align_items="center",
            ),
            max_width="1200px",
            margin="0 auto",
            width="100%",
        ),
        
        # Full-width background matching header
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
        },
        
        id="gallery-section"
    )