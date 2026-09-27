import datetime
import tkinter.messagebox
def crash(crash_title="Unknow Error",description="Unknow error.",report=False,report_message="This report is unknow.",close=True,box=True):
    if box:
        tkinter.messagebox.showerror(crash_title,description)
    if report:
        tmp_time = datetime.datetime.now()
        temp_time = tmp_time.strftime("%Y-%m-%d-%H-%M-%S")
        with open(f"Crash-Report-{temp_time}.txt","w",encoding="utf-8") as crash_report_item:
            crash_report_item.write(crash_title + "\n\n" + description + "\n\n")
            crash_report_item.write(report_message)
    if close:
        exit()