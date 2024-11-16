import reflex as rx
from prompter import style
from prompter.state import State

def query() -> rx.Component:
    return rx.vstack(
        rx.text_area(
            value=State.question,
            placeholder='Ask a question',
            on_change=State.set_question,
            style=style.textarea_style,
        ),
        rx.button(
            'Ask',
            on_click=State.ask_question,
            color_scheme='grass',
            variant='soft',
            style=style.button_style,
        ),
        style=style.query_style,
    )

def answer() -> rx.Component:
    return rx.card(
        rx.markdown(State.answer),
        style=style.answer_style,
    )

def index() -> rx.Component:
    return rx.box(
        rx.hstack(
            rx.heading(
                "Prompter",
                as_='h1',
                style=style.heading,
            ),
            rx.spacer(),
            rx.button(
                rx.color_mode_cond(
                    light=rx.icon('sun'),
                    dark=rx.icon('moon'),
                ),
                on_click=rx.toggle_color_mode,
                variant='ghost',
            ),
            width='100%',
            justify='space-between',
        ),
        rx.select(
            ['Meta-Llama-3-8B-Instruct'],
            default_value='Meta-Llama-3-8B-Instruct',
            on_change=State.set_model,
            style=style.select,
        ),
        rx.hstack(
            query(),
            answer(),
        ),
        style=style.global_style,
    )

app = rx.App()
app.add_page(index)
