import tkinter as tk
import math

from numpy import append

SMALL_FONT_STYLE = ("Arial", 16)
LARGE_FONT_STYLE = ("Arial", 40, "bold")
DIGITS_FONT_STYLE = ("Arial", 24, 'bold')
DEFAULT_FONT_STYLE = ("Arial", 20)

OFF_WHITE = '#F8FAFF'
WHITE = '#FFFFFF'
LIGHT_BLUE = '#CCEDFF'
LIGHT_GRAY = '#D3D3D3'
LABEL_COLOR = '#25265E'


# here i am creating the main class of the calculator
class Calculator:

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry('500x600')
        self.window.resizable(0, 0)
        self.window.title("Calculator")

        self.total_expression = ''
        self.current_expression = ''

        self.display_frame = self.create_display_frame()
        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (5, 2), 8: (5, 3), 9: (5, 4),
            4: (6, 2), 5: (6, 3), 6: (6, 4),
            1: (7, 2), 2: (7, 3), 3: (7, 4),
            0: (8, 3), '.': (8, 4)
        }

        self.operators = {
            "%": "%",
            "/": "÷",
            "*": "×",
            "-": "-",
            "+": "+"
        }

        self.buttons_frame = self.create_buttons_frame()
        self.create_buttons()
        self.buttons_frame.rowconfigure(0, weight=1)
        self.bind_keys()

        for x in range(1, 8):
            self.buttons_frame.rowconfigure(x, weight=1)
        for n in range(1, 5):
            self.buttons_frame.columnconfigure(n, weight=1)

    # Here I create the functions for creating frames and labels
    def create_display_frame(self):
        frame = tk.Frame(self.window, height='370', bg=LIGHT_GRAY)
        frame.pack(expand=True, fill='both')
        return frame

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill='both')
        return frame

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E,
                               bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill='both')

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E,
                         bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill='both')

        return total_label, label

    # Here I want to create the button-creating functions

    # Buttons for basic operations
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR,
                               font=DIGITS_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 3
        for operator, symbol in self.operators.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=operator: self.append_operator(x))
            button.grid(row=i, column=5, sticky=tk.NSEW)
            i += 1

    def create_clear_buttons(self):
        button1 = tk.Button(self.buttons_frame, text='CE', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.clear_entry)
        button1.grid(row=4, column=2, sticky=tk.NSEW)

        button = tk.Button(self.buttons_frame, text='C', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=4, column=3, sticky=tk.NSEW)

    def create_del_button(self):
        button = tk.Button(self.buttons_frame, text='\u232B', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.delete)
        button.grid(row=4, column=4, sticky=tk.NSEW)

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text='=', bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=8, column=5, sticky=tk.NSEW)

    # Buttons for more advanced calculations
    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text='x²', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.square)
        button.grid(row=2, column=1, sticky=tk.NSEW)

    def create_power_button(self):
        button = tk.Button(self.buttons_frame, text='x\u02b8', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.power)
        button.grid(row=2, column=2, sticky=tk.NSEW)

    def create_sin_button(self):
        button = tk.Button(self.buttons_frame, text='sin', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.sinus)
        button.grid(row=2, column=3, sticky=tk.NSEW)

    def create_cos_button(self):
        button = tk.Button(self.buttons_frame, text='cos', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.cosinus)
        button.grid(row=2, column=4, sticky=tk.NSEW)

    def create_tan_button(self):
        button = tk.Button(self.buttons_frame, text='tan', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.tangens)
        button.grid(row=2, column=5, sticky=tk.NSEW)

    def create_square_root_button(self):
        button = tk.Button(self.buttons_frame, text='√x', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.square_root)
        button.grid(row=3, column=1, sticky=tk.NSEW)

    def create_power10_button(self):
        button = tk.Button(self.buttons_frame, text='10\u02e3', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.power_10)
        button.grid(row=3, column=2, sticky=tk.NSEW)

    def create_log_button(self):
        button = tk.Button(self.buttons_frame, text='lg', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.log)
        button.grid(row=3, column=3, sticky=tk.NSEW)

    def create_exp_button(self):
        button = tk.Button(self.buttons_frame, text='Exp', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.exp)
        button.grid(row=3, column=4, sticky=tk.NSEW)

    def create_reciproc_button(self):
        button = tk.Button(self.buttons_frame, text='\u00b9\u2044\u2093', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.reciproc)
        button.grid(row=4, column=1, sticky=tk.NSEW)

    def create_pi_button(self):
        button = tk.Button(self.buttons_frame, text='𝜋', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.display_pi)
        button.grid(row=5, column=1, sticky=tk.NSEW)

    def create_fact_button(self):
        button = tk.Button(self.buttons_frame, text='n!', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.fact)
        button.grid(row=6, column=1, sticky=tk.NSEW)

    def create_switch_sign_button(self):
        button = tk.Button(self.buttons_frame, text='±', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.switch_sign)
        button.grid(row=7, column=1, sticky=tk.NSEW)

    def create_deg_button(self):
        button = tk.Button(self.buttons_frame, text='Deg', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.degree)
        button.grid(row=8, column=1, sticky=tk.NSEW)

    def create_rad_button(self):
        button = tk.Button(self.buttons_frame, text='Rad', bg=WHITE, fg=LABEL_COLOR,
                           font=DIGITS_FONT_STYLE, borderwidth=0, command=self.radians)
        button.grid(row=8, column=2, sticky=tk.NSEW)

    # Here I create methods that combine the previous ones so that the __init__ method looks more neat
    def create_buttons(self):
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_buttons()
        self.create_equals_button()
        self.create_del_button()
        self.create_special_buttons()
        self.create_memory_buttons()

    def create_special_buttons(self):
        self.create_square_button()
        self.create_square_root_button()
        self.create_pi_button()
        self.create_fact_button()
        self.create_reciproc_button()
        self.create_switch_sign_button()
        self.create_power_button()
        self.create_power10_button()
        self.create_log_button()
        self.create_exp_button()
        self.create_deg_button()
        self.create_rad_button()
        self.create_sin_button()
        self.create_cos_button()
        self.create_tan_button()

    # Here I want to create additional functions that help me with the labels/expressions.

    # Methods for updating the labels
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operators.items():
            expression = expression.replace(operator, symbol)
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    # Methods for manipulating the labels
    def add_to_total_expression(self, value):
        self.total_expression += str(value)
        self.update_total_label()

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = ''
        self.update_total_label()
        self.update_label()

    # Methods for clearing/deleting the labels/information
    def clear(self):
        self.current_expression = ''
        self.total_expression = ''
        self.update_label()
        self.update_total_label()

    def clear_entry(self):
        self.total_expression = self.current_expression
        self.update_total_label()
        self.current_expression = ''
        self.update_label()

    def delete(self):
        if self.current_expression == "":
            self.total_expression = self.total_expression[:-1]
            self.update_total_label()
        self.current_expression = self.current_expression[:-1]
        self.update_label()

    # Here i want to create the special operator functions for more advanced calculations
    def square(self):
        self.current_expression = str(eval(f'{self.current_expression}**2'))
        self.update_label()

    def display_pi(self):
        self.current_expression = str(eval(f'{self.current_expression}*math.pi'))
        self.update_label()

    def reciproc(self):
        self.current_expression = str(eval(f'1/{self.current_expression}'))
        self.update_label()

    def square_root(self):
        self.current_expression = str(eval(f'math.sqrt({self.current_expression})'))
        self.update_label()

    def fact(self):
        self.current_expression = str(eval(f'math.factorial({self.current_expression})'))
        self.update_label()

    def switch_sign(self):
        self.current_expression = str(eval(f'-1*{self.current_expression}'))
        self.update_label()

    def power(self):
        try:
            self.total_expression = ''
            self.update_total_label()
            self.append_operator('**')
            self.add_to_total_expression(self.current_expression)
            self.current_expression = str(eval(f'{self.total_expression}'))
        except SyntaxError:
            pass

    def power_10(self):
        self.current_expression = str(eval(f'10**{self.current_expression}'))
        self.update_label()

    # I had a problem with making the base of the logarithm a number,chosen by the user,so I opted for a base of 10
    def log(self):
        try:
            self.current_expression = str(eval(f'math.log10({self.current_expression})'))
        except ValueError:
            self.current_expression = 'Error'
        finally:
            self.update_label()

    def exp(self):
        self.current_expression = str(eval(f'math.exp({self.current_expression})'))
        self.update_label()

    # Here I didn't know whether to create a radiobutton/menubutton with the deg/rad option , so I just went for a converter between the two entities.
    def degree(self):
        self.current_expression = str(eval(f'math.degrees({self.current_expression})'))
        self.update_label()

    def radians(self):
        self.current_expression = str(eval(f'math.radians({self.current_expression})'))
        self.update_label()

    # My trigonometry functions work only with degrees.I didn't know if it should have been plain numbers/rad.
    def sinus(self):
        self.current_expression = str(eval(f'math.sin(math.radians({self.current_expression}))'))
        self.update_label()

    def cosinus(self):
        self.current_expression = str(eval(f'math.cos(math.radians({self.current_expression}))'))
        self.update_label()

    def tangens(self):
        self.current_expression = str(eval(f'math.tan(math.radians({self.current_expression}))'))
        self.update_label()

    # Method for calculating and displaying the results
    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:
            self.current_expression = str(eval(self.total_expression))
            self.total_expression = ''

        except Exception as e:
            self.current_expression = 'Error'

        finally:
            self.update_label()

            # Here I want to create the memory functions and buttons

    memory = 0.0

    def memory_reminder(self):
        self.current_expression = str(self.memory)
        self.update_label()

    def add_to_memory(self):
        self.memory = self.memory + float(self.current_expression)
        self.total_expression = ""
        self.update_total_label()

    def subtract_from_memory(self):
        self.memory = self.memory - float(self.current_expression)
        self.total_expression = ""
        self.update_total_label()

    def memory_clear(self):
        self.memory = 0

    def memory_set(self):
        self.memory = float(self.current_expression)
        self.total_expression = ""
        self.update_total_label()

    def create_memory_buttons(self):
        button1 = tk.Button(self.buttons_frame, text='MC', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.memory_clear)
        button1.grid(row=1, column=1, sticky=tk.NSEW)

        button2 = tk.Button(self.buttons_frame, text='MR', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.memory_reminder)
        button2.grid(row=1, column=2, sticky=tk.NSEW)

        button3 = tk.Button(self.buttons_frame, text='M+', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.add_to_memory)
        button3.grid(row=1, column=3, sticky=tk.NSEW)

        button4 = tk.Button(self.buttons_frame, text='M-', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.subtract_from_memory)
        button4.grid(row=1, column=4, sticky=tk.NSEW)

        button5 = tk.Button(self.buttons_frame, text='MS', bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                            borderwidth=0, command=self.memory_set)
        button5.grid(row=1, column=5, sticky=tk.NSEW)

    # Here I want to bind the digits,equals to and basic operator keys from  the keyboard
    def bind_keys(self):
        self.window.bind('<Return>', lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operators:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    # Here i am creating the mainloop method for the class
    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()
