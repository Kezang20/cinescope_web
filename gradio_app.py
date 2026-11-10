"""CineScope – Gradio version of the final presentation website.
Run:  python gradio_app.py
"""
import pandas as pd
import gradio as gr
import content as c
 
def md_list(items):
    return "\n".join(f"- {i}" for i in items)
 
THEME = gr.themes.Base(primary_hue="red", neutral_hue="slate").set(
    body_background_fill="#0d0d12", body_text_color="#B17777")
 
with gr.Blocks(title="CineScope · Movie & TV Explorer") as demo:
    gr.HTML(c.hero())
 
    with gr.Tabs():
        with gr.Tab("Team"):
            gr.HTML(c.team_html())
 
        with gr.Tab("Problem & Solution"):
            with gr.Row():
                gr.Markdown("## The problem\n" + md_list(c.PROBLEM))
                gr.Markdown("## Our solution\n" + md_list(c.SOLUTION))
            gr.Markdown("## Target users\n" + md_list(c.TARGET_USERS))
 
        with gr.Tab("Features"):
            gr.HTML(c.features_html())
            gr.HTML(c.note(c.FEATURE_NOTE))
 
        with gr.Tab("Architecture"):
            gr.HTML(c.architecture_html())
 
        with gr.Tab("Design Diagrams"):
            with gr.Row():
                gr.Image(str(c.USE_CASE_IMG), label=c.USE_CASE_CAPTION, interactive=False)
                gr.Image(str(c.ERD_IMG), label=c.ERD_CAPTION, interactive=False)
            gr.HTML(c.note(c.ERD_NOTE))
 
        with gr.Tab("GUI & Navigation"):
            gr.HTML(c.gui_html())
 
        with gr.Tab("Live Demo"):
            gr.HTML(c.demo_html())
 
        with gr.Tab("Technologies"):
            gr.Dataframe(pd.DataFrame(c.TECHNOLOGIES, columns=["Technology", "Used for"]),
                         interactive=False, wrap=True)
 
        with gr.Tab("Code Organisation"):
            gr.HTML(c.modules_html())
            gr.HTML(c.note(c.MODULE_NOTE))
            gr.Image(str(c.STRUCTURE_IMG), label="Project structure in VS Code", height=420,
                     interactive=False)
 
            def show_module(name):
                return dict(c.MODULES).get(name, "")
            pick = gr.Dropdown([m for m, _ in c.MODULES], label="Look up a module")
            out = gr.Textbox(label="Responsibility", interactive=False)
            pick.change(show_module, pick, out)
 
        with gr.Tab("Challenges"):
            gr.HTML(c.challenges_html())
 
        with gr.Tab("Testing"):
            gr.HTML(c.testing_html())
 
        with gr.Tab("GitHub & Resources"):
            gr.Markdown(f"## Repository\n[{c.REPO_URL}]({c.REPO_WEB})\n\n" + md_list(c.REPO_POINTS))
            gr.Markdown("## Documentation and sources")
            gr.HTML(c.resources_html())
 
if __name__ == "__main__":
    demo.launch(theme=THEME, css=c.CSS)
 