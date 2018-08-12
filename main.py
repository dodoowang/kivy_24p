from __future__ import division

from kivy.app import App
import kivy

# kivy.require("1.10.0")
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ListProperty
from kivy.clock import Clock

import calc24
from random import randint


class Calc24(BoxLayout):
    nums = ListProperty()

    def update_nums(self, btn):
        if len(self.nums) < 4:
            self.nums.append(int(btn.text))

    def on_nums(self, *args):
        if len(self.nums) == 4:
            self.ids.id_ans.text = "Searching..."
            Clock.schedule_once(self.get_next_solution)

    def get_next_solution(self, *args):
        if self.ids.id_ans.text == "Searching...":
            self.solutions = (x for x in calc24.all_solutions(self.nums))
        next_solution = next(self.solutions, "no solution found")
        if next_solution == "no solution found" \
           and self.ids.id_ans.text != "Searching...":
                return False
        self.ids.id_ans.text = next_solution

    def generate_4_random_nums(self, *args):
        self.nums = [randint(1, 9) for n in range(4)]


class myApp(App):

    def build(self):
        self.title = "24 points"
        self.icon = "icon.png"
        self.load_kv("calc24.kv")
        layout = Calc24()
        return layout


if __name__ == "__main__":
    myApp().run()
