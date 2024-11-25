import tkinter as tk
from tkinter import filedialog, messagebox
from collections import defaultdict
import os

# Побудова графа
def build_graph(numbers):
    graph = defaultdict(list)
    for num1 in numbers:
        suffix = num1[-2:]
        for num2 in numbers:
            if num1 != num2 and suffix == num2[:2]:
                graph[num1].append(num2)
    return graph

# Пошук найдовшого шляху з мемоізацією
def find_longest_path(graph, start, memo, path=[]):
    if start in memo:
        return memo[start]
    longest_path = list(path) + [start]
    for neighbor in graph[start]:
        if neighbor not in path:
            candidate_path = find_longest_path(graph, neighbor, memo, longest_path)
            if len(candidate_path) > len(longest_path):
                longest_path = candidate_path
    memo[start] = longest_path
    return longest_path

# Зчитування файлу
def read_file(filepath):
    with open(filepath, 'r') as file:
        return [line.strip() for line in file.readlines()]

# Обробка даних і результатів
def process_file(filepath):
    numbers = read_file(filepath)
    graph = build_graph(numbers)
    longest_sequence = []
    memo = {}
    for start_node in numbers:
        current_path = find_longest_path(graph, start_node, memo, [])
        if len(current_path) > len(longest_sequence):
            longest_sequence = current_path

    # Побудова результатів
    detailed_result = longest_sequence[0][:4]
    for i in range(1, len(longest_sequence)):
        detailed_result += f"({longest_sequence[i - 1][-2:]}){longest_sequence[i][2:4]}"

    joined_result = longest_sequence[0]
    for num in longest_sequence[1:]:
        joined_result += num[2:]

    return detailed_result, joined_result


# GUI
def main():
    def select_file():
        file_path = filedialog.askopenfilename(
            title="Виберіть файл",
            filetypes=[("Text Files", "*.txt")]
        )
        if not file_path:
            return
        try:
            data = read_file(file_path)
            input_text.delete("1.0", tk.END)
            input_text.insert(tk.END, "\n".join(data))
            detailed_result, joined_result = process_file(file_path)

            print(detailed_result)
            
            result_text.delete("1.0", tk.END)
            result_text.insert(tk.END, detailed_result)
            compact_result_text.delete("1.0", tk.END)
            compact_result_text.insert(tk.END, joined_result)
        except Exception as e:
            messagebox.showerror("Помилка", f"Не вдалося обробити файл: {e}")

    # Створення вікна
    root = tk.Tk()
    root.title("BaD: Задача-пазл")
    root.geometry("600x400")

    tk.Label(root, text="Дані з файлу:").pack()
    input_text = tk.Text(root, height=10, width=70)
    input_text.pack()

    tk.Button(root, text="Вибрати файл", command=select_file).pack()

    tk.Label(root, text="Результат (докладний):").pack()
    result_text = tk.Text(root, height=5, width=70)
    result_text.pack()

    tk.Label(root, text="Результат (компактний):").pack()
    compact_result_text = tk.Text(root, height=2, width=70)
    compact_result_text.pack()

    root.mainloop()

if __name__ == "__main__":
    main()
