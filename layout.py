
CSS_FILE = "../../../../css/darktheme.css"
META_COMMAND = '<meta charset="utf-8" />'
LINK_COMMAND = f'<link rel="stylesheet" href="{CSS_FILE}" type="text/css" />'


def import_commands(file_path):

	with open(file_path, "r") as file:
		content = file.read()
		final_content = "<!DOCTYPE html>\n"
		final_content += "<html>\n<head>\n"
		final_content += META_COMMAND + "\n" + LINK_COMMAND + "\n"
		final_content += "</head>\n<body>\n"
		final_content += content
		final_content += "\n</body>\n</html>"

	with open(file_path, "w") as file:
		file.write(final_content)