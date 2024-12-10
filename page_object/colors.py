def find_color_name(color):
    color_names = {
        "#ffffff": "White",
        "#f29111": "Orange"
    }
    return color_names.get(color)


def css_parameters(property):
    css_properties = {
        "padding": "20px",
        "font-size": "14px"
    }
    return css_properties.get(property)
