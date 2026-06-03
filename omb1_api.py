import math, sqlite3, random

class OMB1UltimateHybridBrain:
    def __init__(self):
        self.db_path = "omb1_final_core.db"
        conn = sqlite3.connect(self.db_path)
        conn.execute('CREATE TABLE IF NOT EXISTS matrix_space (hash REAL PRIMARY KEY, content TEXT, dtype TEXT)')
        conn.commit()
        conn.close()

    def _get_hash(self, text):
        return round(abs(sum(math.sin(ord(c)) for c in text.lower().strip()) * math.pi) % 1, 8)

    def learn(self, input_text, output_data, dtype="text"):
        conn = sqlite3.connect(self.db_path)
        h = self._get_hash(input_text)
        conn.execute("INSERT OR REPLACE INTO matrix_space VALUES (?,?,?)", (h, output_data, dtype))
        conn.commit()
        conn.close()

    def smooth_reply_stream(self, user_input):
        user_input = user_input.lower().strip()
        if "naam" in user_input: return ("Mera naam Sky hai, ZERO Company ka model.", "text")
        
        conn = sqlite3.connect(self.db_path)
        h = self._get_hash(user_input)
        res = conn.execute("SELECT content, dtype FROM matrix_space WHERE hash = ?", (h,)).fetchone()
        conn.close()
        return res if res else ("Data pack mein yeh info nahi hai. Train kariye.", "text")
