# app/app.py

import gradio as gr
from src.rag_pipeline import load_vector_store, answer_query

# Load index, chunks, and metadata once
index, chunks, metadata = load_vector_store()

def chat_with_rag(query):
    answer, sources, _ = answer_query(query, index, chunks, metadata, k=5)

    formatted_sources = "\n\n---\n\n".join(sources[:2])  # show top 2 sources

    return answer.strip(), formatted_sources

# Gradio UI layout
with gr.Blocks() as demo:
    gr.Markdown("# 💬 CrediTrust Complaint Chatbot")
    gr.Markdown("Ask questions about customer complaints. The model will answer based on actual complaint narratives.")

    with gr.Row():
        query_input = gr.Textbox(placeholder="e.g. Why are users unhappy with BNPL?", label="Your Question")
    
    with gr.Row():
        ask_btn = gr.Button("Ask")
        clear_btn = gr.Button("Clear")

    answer_output = gr.Textbox(label="Answer", lines=5)
    source_output = gr.Textbox(label="Retrieved Complaint Chunks", lines=8)

    # Event handlers
    ask_btn.click(fn=chat_with_rag, inputs=[query_input], outputs=[answer_output, source_output])
    clear_btn.click(fn=lambda: ("", ""), inputs=[], outputs=[answer_output, source_output])

# Launch
if __name__ == "__main__":
    demo.launch()
