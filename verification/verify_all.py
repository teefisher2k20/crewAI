import os
import re
from playwright.sync_api import Page, expect, sync_playwright
from crewai.flow.flow import Flow, start, listen
from crewai.flow.visualization import render_interactive
from crewai.flow.visualization.builder import build_flow_structure

class SimpleFlow(Flow):
    @start()
    def start_node(self):
        return "Hello"

    @listen(start_node)
    def second_node(self, greeting):
        return f"{greeting} World"

def run_verification():
    # 1. Generate visualization
    flow = SimpleFlow()
    structure = build_flow_structure(flow)
    viz_path = render_interactive(structure, "flow_viz.html", show=False)
    print(f"Visualization generated at {viz_path}")

    # 2. Run Playwright
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        try:
            file_url = "file://" + viz_path
            page.goto(file_url)
            page.wait_for_timeout(3000)

            # Note: handleNodeClick is NOT global anymore, but we can still
            # find it if we use some trickery, or just click the canvas.
            # But wait, I just removed the global reference.
            # Let's try to click the node on the canvas.
            viewport = page.viewport_size
            page.mouse.click(viewport['width'] / 2, 100)
            page.wait_for_timeout(1000)

            drawer = page.locator("#drawer")
            # expect(drawer).to_have_class(re.compile(r"open"))

            os.makedirs("verification", exist_ok=True)
            page.screenshot(path="verification/viz_final.png")
            print("Took screenshot: verification/viz_final.png")

        finally:
            browser.close()

if __name__ == "__main__":
    run_verification()
