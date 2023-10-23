import re
import time
from command_factory import CommandFactory
import tkinter as tk
from tkinter import ttk


def is_solvable(state):
    # Convert the state string to a list of integers
    state_list = [int(x) for x in re.findall(r'\d', state)]
    # Count the number of inversions
    inversions = 0
    for i in range(len(state_list)):
        for j in range(i + 1, len(state_list)):
            if state_list[i] > state_list[j] != 0 and state_list[i] != 0:
                inversions += 1

    # Check if the number of inversions is even
    if inversions % 2 == 0:
        return True
    else:
        return False

      
class Gui:
    def __init__(self):
        # initialization
        self.time_ans = None
        self.time_label = None
        self.depth_ans = None
        self.depth_label = None
        self.expand_ans = None
        self.expand_label = None
        self.index = None
        self.path = None
        self.cost_ans = None
        self.status_ans = None
        self.cost_label = None
        self.status_label = None
        self.status_frame = None
        self.nav_frame = None
        self.prev_btn = None
        self.next_btn = None
        self.buttons_array = None
        self.ans_frame = None
        self.show_button = None
        self.need_path = None
        self.need_path_value = None
        self.methods = None
        self.chosen_method = None
        self.state_input_box = None
        self.state_input_label = None
        self.input_form = None
        self.root = None
        self.initial_state = None
        self.method = None
        self.with_parents = None
        # show gui
        self.show_window()

    def show_window(self):
        # setting window
        self.with_parents = None
        self.method = None
        self.initial_state = None
        self.root = tk.Tk()
        self.root.geometry("800x600")
        self.root.title("8-Puzzle")
        self.root.configure(bg='#856ff8')
        # input frame
        self.input_form = tk.Frame(self.root, background='#856ff8')
        self.input_form.columnconfigure(0, weight=1)
        self.input_form.columnconfigure(1, weight=1)
        # input elements
        # first row
        self.state_input_label = tk.Label(self.input_form,
                                          text="Enter initial state",
                                          font="20",
                                          background='#856ff8')
        self.state_input_label.grid(row=0, column=0, sticky=tk.W + tk.E)
        self.state_input_box = tk.Text(self.input_form, height=2)
        self.state_input_box.grid(row=0, column=1, sticky=tk.W + tk.E, padx=10, pady=20)
        # second row
        self.chosen_method = tk.StringVar()
        self.methods = ttk.Combobox(self.input_form, textvariable=self.chosen_method)
        self.methods.grid(row=1, column=1)
        self.methods['values'] = ['dfs', 'bfs', 'Manhattan', 'Euclidean']
        self.methods['state'] = 'readonly'
        # third row
        self.need_path_value = tk.IntVar()
        self.need_path = tk.Checkbutton(self.input_form,
                                        text="Print the path to the solution",
                                        font="20",
                                        background='#856ff8',
                                        variable=self.need_path_value)
        self.need_path.grid(row=2, column=1, padx=20)
        # forth row
        self.show_button = tk.Button(self.input_form,
                                     text="Show solution",
                                     font="20",
                                     activebackground='red',
                                     background='#999999',
                                     command=self.on_submit)
        self.show_button.grid(row=3, column=1, pady=10)
        self.input_form.pack()
        self.root.mainloop()

    def on_submit(self):
        self.initial_state, self.method, self.with_parents = (self.state_input_box.get('1.0', tk.END)[:9],
                                                              self.chosen_method.get(), self.need_path_value.get())
        # initial_node = Node.Node(self.initial_state, 0)
        command = CommandFactory.create_commands(self.method, self.initial_state, self.with_parents)
        start_time = time.time()
        status, description = command.execute()
        end_time = time.time()
        print("Time taken: ", end_time - start_time)
        self.show_main_data(status, description[0], description[1], description[2], end_time - start_time)
        if self.with_parents:
            self.path = description[-1]
            self.index = 0
            self.show_results_buttons()

    def show_main_data(self, status, cost, expanded, depth, my_time):
        self.status_frame = tk.Frame(self.root, background='#856ff8')
        self.status_frame.columnconfigure(0, weight=1)
        self.status_frame.columnconfigure(1, weight=1)
        self.status_label = tk.Label(self.status_frame,
                                     text="Status:",
                                     font="20",
                                     background='#856ff8')
        self.status_label.grid(row=0, column=0, padx=20)
        self.status_ans = tk.Label(self.status_frame,
                                   text=status,
                                   font="20",
                                   foreground="#00FF00",
                                   background='#856ff8')
        self.status_ans.grid(row=0, column=1, padx=20)
        self.cost_label = tk.Label(self.status_frame,
                                   text="Cost:",
                                   font="20",
                                   background='#856ff8')
        self.cost_label.grid(row=1, column=0, padx=20)
        self.cost_ans = tk.Label(self.status_frame,
                                 text=cost,
                                 font="20",
                                 background='#856ff8')
        self.cost_ans.grid(row=1, column=1, padx=20)
        self.expand_label = tk.Label(self.status_frame,
                                     text="#Expadned:",
                                     font="20",
                                     background='#856ff8')
        self.expand_label.grid(row=2, column=0, padx=20)
        self.expand_ans = tk.Label(self.status_frame,
                                   text=expanded,
                                   font="20",
                                   background='#856ff8')
        self.expand_ans.grid(row=2, column=1, padx=20)
        self.depth_label = tk.Label(self.status_frame,
                                    text="Max depth:",
                                    font="20",
                                    background='#856ff8')
        self.depth_label.grid(row=3, column=0, padx=20)
        self.depth_ans = tk.Label(self.status_frame,
                                  text=depth,
                                  font="20",
                                  background='#856ff8')
        self.depth_ans.grid(row=3, column=1, padx=20)
        self.time_label = tk.Label(self.status_frame,
                                   text="Time(sec):",
                                   font="20",
                                   background='#856ff8')
        self.time_label.grid(row=4, column=0, padx=20)
        self.time_ans = tk.Label(self.status_frame,
                                 text=(round(my_time, 5)),
                                 font="20",
                                 background='#856ff8')
        self.time_ans.grid(row=4, column=1, padx=20)
        self.status_frame.pack()

    def show_results_buttons(self):
        # state show frame
        self.ans_frame = tk.Frame(self.root, background='#856ff8')
        for i in range(3):
            self.ans_frame.columnconfigure(i, weight=1)
        self.buttons_array = []
        for i in range(3):
            for j in range(3):
                self.buttons_array.append(tk.Button(self.ans_frame,
                                                    text=self.path[0][i * 3 + j],
                                                    font="20",
                                                    background='#999999'))
                self.buttons_array[-1].grid(row=i, column=j, padx=5, pady=5)
        self.ans_frame.pack(pady=20)
        # navigation buttons frame
        self.nav_frame = tk.Frame(self.root, background='#856ff8')
        self.nav_frame.columnconfigure(0, weight=1)
        self.nav_frame.columnconfigure(1, weight=1)
        self.prev_btn = tk.Button(self.nav_frame, text="PREV", font="20", background='#999999', command=self.prev_step)
        self.next_btn = tk.Button(self.nav_frame, text="NEXT", font="20", background='#999999', command=self.next_step)
        self.prev_btn.grid(row=5, column=0, padx=5, pady=5)
        self.next_btn.grid(row=5, column=1, padx=5, pady=5)
        self.nav_frame.pack(pady=20)

    def prev_step(self):
        if self.index != 0:
            self.index -= 1
            for i in range(3):
                for j in range(3):
                    self.buttons_array[i * 3 + j].config(text=(self.path[self.index][i * 3 + j]))

    def next_step(self):
        if self.index != len(self.path) - 1:
            self.index += 1
            for i in range(3):
                for j in range(3):
                    self.buttons_array[i * 3 + j].config(text=(self.path[self.index][i * 3 + j]))


if __name__ == '__main__':
    Gui()
