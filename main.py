

print("Conflict resolved")

a=7
        def on_date_selected():
            selected_date = cal.selection_get()
            task_listbox.set(selected_task_index, column=2, value=selected_date)
            top.destroy()

        top = Toplevel(root)
        top.grab_set()  # pop-up window of the calender

        cal = Calendar(top, selectmode='day', day=4, month=3, year=2024)
        cal.pack(pady=20)

        ok_button = tk.Button(top, text="OK", command=on_date_selected)
        ok_button.pack()


a=5

