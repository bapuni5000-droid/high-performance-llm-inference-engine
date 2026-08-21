import tkinter as tk
from tkinter import ttk
import time

BG="#0b0f14"; PANEL="#121821"; LINE="#27313d"; TEXT="#e6edf3"; MUTED="#7f8b9a"; ACCENT="#62d99a"

class App(tk.Tk):
    def __init__(self):
        super().__init__(); self.title("Inference Lab"); self.geometry("1120x700"); self.configure(bg=BG); self._ui()
    def _ui(self):
        s=ttk.Style(self); s.theme_use("clam"); s.configure("TFrame",background=BG); s.configure("TLabel",background=BG,foreground=TEXT); s.configure("TButton",padding=8)
        nav=tk.Frame(self,bg=PANEL,width=220); nav.pack(side="left",fill="y")
        tk.Label(nav,text="INFERENCE LAB",bg=PANEL,fg=TEXT,font=("Segoe UI",15,"bold")).pack(anchor="w",padx=22,pady=(28,34))
        for label in ["Playground","Benchmark","Runtime","Logs"]: tk.Label(nav,text=label,bg=PANEL,fg=TEXT if label=="Playground" else MUTED,font=("Segoe UI",11),anchor="w").pack(fill="x",padx=22,pady=9)
        tk.Frame(nav,bg=LINE,height=1).pack(fill="x",padx=18,pady=25)
        tk.Label(nav,text="RUNTIME",bg=PANEL,fg=MUTED,font=("Segoe UI",9,"bold")).pack(anchor="w",padx=22)
        self.runtime=tk.Label(nav,text="●  Ready",bg=PANEL,fg=ACCENT,font=("Segoe UI",10)); self.runtime.pack(anchor="w",padx=22,pady=10)
        body=tk.Frame(self,bg=BG); body.pack(fill="both",expand=True,padx=25,pady=22)
        top=tk.Frame(body,bg=BG); top.pack(fill="x")
        tk.Label(top,text="Model playground",bg=BG,fg=TEXT,font=("Segoe UI",23,"bold")).pack(side="left")
        tk.Label(top,text="C++ runtime / demo",bg=BG,fg=MUTED,font=("Segoe UI",10)).pack(side="left",padx=15,pady=10)
        controls=tk.Frame(body,bg=PANEL,highlightbackground=LINE,highlightthickness=1); controls.pack(fill="x",pady=22)
        self._control(controls,"Threads",tk.IntVar(value=4),1,64,0); self._control(controls,"Max tokens",tk.IntVar(value=64),1,512,1)
        self.quant=tk.StringVar(value="FP16"); tk.Label(controls,text="Quantization",bg=PANEL,fg=MUTED).grid(row=0,column=2,padx=(20,5),pady=14); ttk.Combobox(controls,textvariable=self.quant,values=["FP32","FP16","INT8"],state="readonly",width=10).grid(row=0,column=3,padx=5)
        promptbox=tk.Frame(body,bg=PANEL); promptbox.pack(fill="x")
        tk.Label(promptbox,text="PROMPT",bg=PANEL,fg=MUTED,font=("Segoe UI",9,"bold")).pack(anchor="w",padx=16,pady=(14,5))
        self.prompt=tk.Text(promptbox,height=5,bg="#0f141b",fg=TEXT,insertbackground=TEXT,relief="flat",padx=12,pady=10); self.prompt.pack(fill="x",padx=12,pady=(0,12)); self.prompt.insert("1.0","Explain how KV caching improves transformer inference.")
        tk.Button(body,text="Run inference  →",command=self.run,bg=ACCENT,fg="#07120b",relief="flat",font=("Segoe UI",10,"bold"),padx=18,pady=8).pack(anchor="w",pady=14)
        out=tk.Frame(body,bg=PANEL); out.pack(fill="both",expand=True)
        tk.Label(out,text="OUTPUT",bg=PANEL,fg=MUTED,font=("Segoe UI",9,"bold")).pack(anchor="w",padx=16,pady=(14,5))
        self.output=tk.Text(out,bg="#0f141b",fg=TEXT,relief="flat",wrap="word",padx=14,pady=12); self.output.pack(fill="both",expand=True,padx=12,pady=(0,12))
        self.metrics=tk.Label(body,text="Latency  —     Tokens/s  —     Threads  4",bg=BG,fg=MUTED); self.metrics.pack(anchor="w",pady=9)
    def _control(self,parent,label,var,lo,hi,col):
        tk.Label(parent,text=label,bg=PANEL,fg=MUTED).grid(row=0,column=col*2,padx=(18,5),pady=14)
        ttk.Spinbox(parent,from_=lo,to=hi,textvariable=var,width=8).grid(row=0,column=col*2+1,padx=5)
    def run(self):
        t=time.perf_counter(); q=self.prompt.get("1.0","end").strip(); time.sleep(.03)
        self.output.delete("1.0","end"); self.output.insert("1.0",f"Demo runtime response\n\n{q}\n\nThis panel is ready to be connected to the C++ inference path.")
        dt=time.perf_counter()-t; self.metrics.config(text=f"Latency  {dt*1000:.1f} ms     Tokens/s  {64/dt:.1f}     Threads  4")
if __name__=="__main__": App().mainloop()
