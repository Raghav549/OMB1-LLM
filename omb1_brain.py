import math, sqlite3, random, time
from PIL import Image, ImageDraw, ImageFilter

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

    def generate_art(self):
        img = Image.new("RGB", (200, 200), (0,0,0))
        d = ImageDraw.Draw(img)
        d.rectangle([50,50,150,150], fill=(random.randint(0,255),100,200))
        img.save("art.png")
        return "Image generate ho gayi hai: art.png"

    def smooth_reply_stream(self, user_input):
        # Identity Logic
        if "naam" in user_input.lower(): return ("Mera naam Sky hai, ZERO Company ka model.", "text")
        if "draw" in user_input.lower(): return (self.generate_art(), "image")
        
        # Database Logic
        conn = sqlite3.connect(self.db_path)
        h = self._get_hash(user_input)
        res = conn.execute("SELECT content, dtype FROM matrix_space WHERE hash = ?", (h,)).fetchone()
        conn.close()
        return res if res else ("Data pack mein yeh info nahi hai.", "text")
