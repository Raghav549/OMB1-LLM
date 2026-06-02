# ==========================================
# COMPANY: ZERO | MODEL: OMB1
# MODULE: DATA ADHIGHRAHAM (File Ingester)
# COST: ZERO (Local Directory Stream)
# ==========================================

import os
from omb1_core import OMB1_Model

def external_file_loader(model_instance, file_name):
    """
    Local storage se .txt file ko read karke 
    OMB1 model ke infinity matrix mein instantly load karna.
    """
    if os.path.exists(file_name):
        print(f"\n[Scanning] Local file '{file_name}' ko process kiya ja raha hai...")
        
        with open(file_name, "r", encoding="utf-8") as f:
            raw_data = f.read().strip()
            
        if not raw_data:
            print("❌ [Error]: File khali hai.")
            return
            
        model_instance.tatkal_grahanam(file_name, raw_data)
    else:
        print(f"❌ [Error]: '{file_name}' file nahi mili.")

if __name__ == "__main__":
    mymodel = OMB1_Model()
    external_file_loader(mymodel, "gyan_input.txt")
