# ==========================================
# COMPANY: ZERO | MODEL: OMB1
# MODULE: SUTRA STHANAM (Interactive Shell)
# COST: ZERO (100% Mobile Offline Console)
# ==========================================

import os
from omb1_core import OMB1_Model
from data_adhigraham import external_file_loader

def main_dashboard():
    omb1 = OMB1_Model()
    
    print("\n=========================================")
    print("      ZERO - OMB1 INTERACTIVE CONSOLE     ")
    print("=========================================")
    print("निर्देश (Commands):")
    print(" 1. load <filename>  -> Text file ko system mein catch karwana")
    print(" 2. ask <query>      -> Sanskrit model se prashna poochna")
    print(" 3. exit             -> Console ko band karna")
    print("=========================================\n")

    while True:
        try:
            user_input = input("ZERO-OMB1> ").strip()
            if not user_input:
                continue

            if user_input.lower() == "exit":
                print("🛑 OMB1 Session Samaptaः।")
                break

            elif user_input.startswith("load "):
                file_name = user_input.split(" ", 1)[1].strip()
                external_file_loader(omb1, file_name)

            elif user_input.startswith("ask "):
                query = user_input.split(" ", 1)[1].strip()
                response = omb1.vikas_khoj(query)
                print(response)

            else:
                print("❌ Invalid Command! Use: load <file>, ask <query>, or exit")

        except Exception as e:
            print(f"❌ Error occurred: {e}")

if __name__ == "__main__":
    main_dashboard()
