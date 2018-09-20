def heading_generator(title, heading_type):
    """Dynamically generate HTML heading"""
    return(f"<h{heading_type}>{title}</h{heading_type}>")

print(heading_generator("Hello World", heading_type=1))
