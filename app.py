import customtkinter as ctk


ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

BACKGROUND = "#0B1020"
PANEL = "#141B2D"
PANEL_ACCENT = "#19243A"
TEXT = "#F4F7FC"
MUTED = "#9AA8BD"
BLUE = "#3978F6"


def show_message(label, message, color=MUTED):
    label.configure(text=message, text_color=color)


def register():
    name = name_entry.get().strip()
    email = signup_email_entry.get().strip()
    password = signup_password_entry.get()
    confirmation = confirmation_entry.get()

    if not all((name, email, password, confirmation)):
        show_message(signup_message, "Preencha todos os campos.", "#F5A3A3")
    elif password != confirmation:
        show_message(signup_message, "As senhas não coincidem.", "#F5A3A3")
    else:
        show_message(
            signup_message,
            "Dados validados. Conecte o cadastro para continuar.",
        )


def login():
    email = login_email_entry.get().strip()
    password = login_password_entry.get()

    if not email or not password:
        show_message(login_message, "Informe seu e-mail e sua senha.", "#F5A3A3")
    else:
        show_message(
            login_message,
            "Dados preenchidos. Conecte o login para continuar.",
        )


app = ctk.CTk()
app.title("Locavia | Acesso")
app.geometry("1100x760")
app.minsize(900, 680)
app.configure(fg_color=BACKGROUND)

app.grid_columnconfigure(0, weight=1)
app.grid_rowconfigure(1, weight=1)

header = ctk.CTkFrame(app, fg_color="transparent")
header.grid(row=0, column=0, sticky="ew", padx=52, pady=(34, 22))
header.grid_columnconfigure(0, weight=1)

brand = ctk.CTkLabel(
    header,
    text="LOCAVIA",
    font=("Helvetica", 26, "bold"),
    text_color=TEXT,
)
brand.grid(row=0, column=0, sticky="w")

subtitle = ctk.CTkLabel(
    header,
    text="Entre na sua conta ou crie uma nova para continuar.",
    font=("Helvetica", 14),
    text_color=MUTED,
)
subtitle.grid(row=1, column=0, sticky="w", pady=(5, 0))

content = ctk.CTkFrame(app, fg_color="transparent")
content.grid(row=1, column=0, sticky="nsew", padx=52, pady=(0, 42))
content.grid_columnconfigure((0, 1), weight=1, uniform="panels")
content.grid_rowconfigure(0, weight=1)

signup_panel = ctk.CTkFrame(
    content,
    fg_color=PANEL_ACCENT,
    corner_radius=22,
    border_width=1,
    border_color="#25334D",
)
signup_panel.grid(row=0, column=0, sticky="nsew", padx=(0, 12))
signup_panel.grid_columnconfigure(0, weight=1)

login_panel = ctk.CTkFrame(
    content,
    fg_color=PANEL,
    corner_radius=22,
    border_width=1,
    border_color="#25334D",
)
login_panel.grid(row=0, column=1, sticky="nsew", padx=(12, 0))
login_panel.grid_columnconfigure(0, weight=1)

signup_title = ctk.CTkLabel(
    signup_panel,
    text="Crie sua conta",
    font=("Helvetica", 25, "bold"),
    text_color=TEXT,
)
signup_title.grid(row=0, column=0, sticky="w", padx=34, pady=(34, 5))

signup_description = ctk.CTkLabel(
    signup_panel,
    text="Preencha seus dados para começar.",
    font=("Helvetica", 14),
    text_color=MUTED,
)
signup_description.grid(row=1, column=0, sticky="w", padx=34, pady=(0, 24))


def add_field(parent, label_text, placeholder, row, show=None):
    field_label = ctk.CTkLabel(
        parent,
        text=label_text,
        font=("Helvetica", 13, "bold"),
        text_color="#D7DFEC",
    )
    field_label.grid(row=row, column=0, sticky="w", padx=34, pady=(0, 7))

    entry = ctk.CTkEntry(
        parent,
        height=46,
        corner_radius=10,
        placeholder_text=placeholder,
        show=show,
        border_color="#34425B",
        fg_color="#10182A",
        text_color=TEXT,
    )
    entry.grid(row=row + 1, column=0, sticky="ew", padx=34, pady=(0, 16))
    return entry


name_entry = add_field(signup_panel, "Nome completo", "Como podemos te chamar?", 2)
signup_email_entry = add_field(
    signup_panel, "E-mail", "seuemail@exemplo.com", 4
)
signup_password_entry = add_field(
    signup_panel, "Senha", "Crie uma senha", 6, show="*"
)
confirmation_entry = add_field(
    signup_panel, "Confirmar senha", "Digite a senha novamente", 8, show="*"
)

signup_message = ctk.CTkLabel(
    signup_panel,
    text=" ",
    font=("Helvetica", 12),
    text_color=MUTED,
    wraplength=390,
)
signup_message.grid(row=10, column=0, sticky="w", padx=34, pady=(0, 8))

signup_button = ctk.CTkButton(
    signup_panel,
    text="Cadastrar",
    height=48,
    corner_radius=10,
    font=("Helvetica", 15, "bold"),
    fg_color=BLUE,
    hover_color="#2D68DE",
    command=register,
)
signup_button.grid(row=11, column=0, sticky="ew", padx=34, pady=(0, 34))

login_title = ctk.CTkLabel(
    login_panel,
    text="Que bom te ver!",
    font=("Helvetica", 25, "bold"),
    text_color=TEXT,
)
login_title.grid(row=0, column=0, sticky="w", padx=34, pady=(34, 5))

login_description = ctk.CTkLabel(
    login_panel,
    text="Acesse sua conta para continuar.",
    font=("Helvetica", 14),
    text_color=MUTED,
)
login_description.grid(row=1, column=0, sticky="w", padx=34, pady=(0, 24))

login_email_entry = add_field(
    login_panel, "E-mail", "seuemail@exemplo.com", 2
)
login_password_entry = add_field(
    login_panel, "Senha", "Digite sua senha", 4, show="*"
)

remember_me = ctk.CTkCheckBox(
    login_panel,
    text="Manter conectado",
    font=("Helvetica", 13),
    text_color=MUTED,
    fg_color=BLUE,
    hover_color="#2D68DE",
    border_color="#53627A",
)
remember_me.grid(row=6, column=0, sticky="w", padx=34, pady=(0, 24))

login_message = ctk.CTkLabel(
    login_panel,
    text=" ",
    font=("Helvetica", 12),
    text_color=MUTED,
    wraplength=390,
)
login_message.grid(row=7, column=0, sticky="w", padx=34, pady=(0, 8))

login_button = ctk.CTkButton(
    login_panel,
    text="Entrar",
    height=48,
    corner_radius=10,
    font=("Helvetica", 15, "bold"),
    fg_color="#26344D",
    hover_color="#334563",
    command=login,
)
login_button.grid(row=8, column=0, sticky="ew", padx=34, pady=(0, 34))

app.mainloop()
