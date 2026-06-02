# =====================================================================
# COMPANY: ZERO | MODEL: OMB1 (OM BRAHMANANDA 1)
# MODULE: ULTIMATE COGNITIVE REASONING ENGINE (100% LOCAL & INDEPENDENT)
# =====================================================================

import math
import re
import time
import json
import random
from PIL import Image, ImageDraw, ImageFilter, ImageEnhance

class OMB1UltimateHybridBrain:
    def __init__(self):
        # ♾️ Infinity Store Matrix Grid (Pure Local RAM Cluster)
        self.matrix_grid = {}
        self.visual_memory = {}
        self.stop_words = {"hai", "hu", "hun", "ho", "aap", "ko", "ka", "ki", "ke", "mein", "se", "aur", "ek", "is", "am", "are", "you", "the", "this", "to", "kya", "batao", "batayein"}
        self.evolution_registry = {
            "total_cycles": 0,
            "engine_state": "MAX_COGNITION",
            "model_name": "OMB1 (Sky)"
        }

        print("\n" + "🕉️ " * 15)
        print("ZERO COMPANY | OMB1 ULTIMATE TAGDA LLM CORE ACTIVE")
        print("PI-LOGIC & INFINITY STORE OPERATIONAL WITHOUT EXTERNAL APIS")
        print("🕉️ " * 15 + "\n")

    def _varna_matrix_hash(self, text):
        """ Core Pi-Logic Wave Math Address Calculator """
        if not text: return 0.0
        scores = [ord(c) for c in text]
        wave = sum(math.sin(s) * 1.618 for s in scores)
        return round(abs(wave * math.pi) % 1, 8)

    def _tokenize(self, text):
        """ Tokenizes text for deep context mapping """
        return list(set(re.findall(r'[a-zA-Z0-9\u0400-\u09FF]{2,}', text.lower())))

    def tatkal_grahanam(self, source, content_stream):
        """ Instant Memory Capture Loop - Saves every single detail permanently """
        start = time.time()
        content_clean = content_stream.strip()
        ptr = self._varna_matrix_hash(content_clean)
        tokens = self._tokenize(content_clean)
        
        # Storing permanently in the infinity matrix grid cluster
        self.matrix_grid[ptr] = {
            "source": source, 
            "data": content_clean, 
            "tokens": tokens, 
            "timestamp": time.time()
        }
        self.evolution_registry["total_cycles"] += 1
        print(f"📥 [Instant Learn] Mapped to Grid -> Ptr: {ptr} | Content: '{content_clean}'")
        return ptr

    def _cognitive_flip_perspective(self, text):
        """ 
        Advanced Reasoning Layer: Flips pronouns dynamically so that 
        user inputs like 'Aapka naam sky hai' become 'Mera naam sky hai'.
        """
        replacements = [
            (r"\baapka naam\b", "mera naam"),
            (r"\btumhara naam\b", "mera naam"),
            (r"\baapka\b", "mera"),
            (r"\btumhara\b", "mera"),
            (r"\baap\b", "main"),
            (r"\btum\b", "main"),
            (r"\bmera naam\b", "aapka naam"),
            (r"\bmera\b", "aapka"),
            (r"\bmain ek\b", "aap ek"),
            (r"\bmain\b", "aap"),
            (r"\bhun\b", "hain"),
            (r"\bhu\b", "hain")
        ]
        
        transformed = text.lower()
        for pattern, repl in replacements:
            transformed = re.sub(pattern, repl, transformed)
            
        # Clean up casing and format
        transformed = transformed.strip()
        if transformed:
            transformed = transformed[0].upper() + transformed[1:]
        return transformed

    def smooth_reply_stream(self, user_query):
        """ Ultimate Reasoning & Retrieval Pipeline """
        start_time = time.time()
        user_query_clean = user_query.strip()
        query_tokens = self._tokenize(user_query_clean)
        
        # 1. Trigger Image Generation if user asks to draw or design
        if any(x in user_query_clean.lower() for x in ["draw", "design", "make image", "photo banao", "banayein"]):
            return self.generate_art_loop(user_query_clean)

        # Filter out common stop words to catch the core concept (e.g., "naam", "sky")
        meaningful_query_tokens = [t for t in query_tokens if t not in self.stop_words]

        best_match_node = None
        max_overlap_score = 0
        
        # 2. Infinite Matrix Grid Scanning Loop
        if meaningful_query_tokens:
            for ptr, node in self.matrix_grid.items():
                if node.get("source") in ["Mool_Sutra", "System_Internal"]:
                    continue
                
                stored_tokens = node.get("tokens", [])
                filtered_stored = [t for t in stored_tokens if t not in self.stop_words]
                
                # Check intersection of meaningful keywords
                overlap = len(set(meaningful_query_tokens).intersection(set(filtered_stored)))
                
                if overlap > max_overlap_score:
                    max_overlap_score = overlap
                    best_match_node = node

        # 3. Dynamic Cognitive Reasoning Decision Maker
        if best_match_node and max_overlap_score >= 1:
            raw_memory = best_match_node.get("data", "")
            # Apply the pronoun flip reasoning layer
            reply = self._cognitive_flip_perspective(raw_memory)
        else:
            # Smart Fallbacks based on standalone pattern matching
            clean_query = user_query_clean.lower()
            if any(x in clean_query for x in ["kaise ho", "how are you"]):
                reply = "Main ekdum badhiya aur high-speed cognition mode mein hoon Raghav bhai! Aapka custom Pi engine super stable chal raha hai."
            elif any(x in clean_query for x in ["who are you", "kaun ho", "identity", "naam kya"]):
                reply = "Main ZERO Company ka flagship model OMB1 hoon. Aap jo bhi mujhe sikhayenge, main use instantly yaad karke reply kar sakta hoon."
            elif any(x in clean_query for x in ["developer", "raghav", "admin"]):
                reply = "Pranam Raghav bhai! Aap is pure system aur ZERO Company ke admin/janmadaata hain. Yeh tathya mere memory store mein permanently locked hai."
            else:
                # Catch-all learning confirmation
                reply = f"OMB1 Matrix Active: Maine aapka input '{user_query_clean}' padh kar, analyze karke local grid cluster mein save kar liya hai. Agli baar main iska use karunga."

        # 4. INSTANT LIVE TRAINING LOOP (Self-Learning on every chat message)
        # If the input looks like a statement (e.g. "Aapka naam sky hai"), save it so it teaches the model instantly!
        if len(meaningful_query_tokens) >= 1 and not user_query_clean.endswith("?"):
            self.tatkal_grahanam("User_Live_Feed", user_query_clean)

        return {
            "source": "ZERO OMB1 Autonomous Brain",
            "reply": reply,
            "speed": f"{(time.time() - start_time)*1000:.2f}ms",
            "matrix_status": "Cognitive Memory Sync Complete"
        }

    # --- ADVANCED GRAPHICS & 3D CANVASES GENERATION ENGINE ---
    def generate_art_loop(self, prompt):
        """ 
        100% Autonomous 3D Canvas, Grids, Graphics, and Ultra-Realistic Color Engine
        Does not use any API. Uses raw trigonometry and coordinate matrix projection.
        """
        start = time.time()
        width, height = 512, 512
        # Initialize a dark modern mathematical grid canvas
        img = Image.new("RGB", (width, height), (10, 15, 25))
        draw = ImageDraw.Draw(img)
        
        # 1. DRAW SYSTEM GRAPHIC GRIDS
        grid_spacing = 32
        for x in range(0, width, grid_spacing):
            draw.line([x, 0, x, height], fill=(25, 35, 50), width=1)
        for y in range(0, height, grid_spacing):
            draw.line([0, y, width, y], fill=(25, 35, 50), width=1)
            
        # 2. MATHEMATICAL 3D PROJECTION GRAPHICS (Spherical/Cubic Mesh Synthesis)
        center_x, center_y = width // 2, height // 2
        num_points = 180
        
        # Synthesize realistic color combinations using mathematical sine frequencies
        for i in range(num_points):
            angle = i * (math.pi / 45)
            # Simulated 3D Z-depth variance using sine waves
            z_depth = math.sin(i * 0.1) * 120
            radius = 140 + z_depth
            
            # Project 3D vector space points onto 2D display canvas
            x1 = int(center_x + radius * math.cos(angle))
            y1 = int(center_y + radius * math.sin(angle) * math.cos(angle * 0.5))
            
            x2 = int(center_x + (radius - 40) * math.cos(angle + 0.2))
            y2 = int(center_y + (radius - 40) * math.sin(angle + 0.2) * math.cos((angle + 0.2) * 0.5))
            
            # Generate vibrant realistic color shades
            r = int((math.sin(i * 0.05) + 1) * 127)
            g = int((math.cos(i * 0.08) + 1) * 127)
            b = int((math.sin(i * 0.12) + 1) * 127)
            
            # Draw architectural mathematical mesh structures
            draw.line([x1, y1, x2, y2], fill=(r, g, b), width=2)
            draw.ellipse([x1-3, y1-3, x1+3, y1+3], fill=(255, 255, 255)) # Coordinate grid nodes

        # 3. HIGH-END GRAPHIC FILTERS & REALISM BLENDING
        img = img.filter(ImageFilter.SMOOTH_MORE)
        img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
        
        # Enhance contrast and saturation for deep, realistic modern colors
        color_enhancer = ImageEnhance.Color(img)
        img = color_enhancer.enhance(1.4)
        contrast_enhancer = ImageEnhance.Contrast(img)
        img = contrast_enhancer.enhance(1.2)
        
        filename = f"render_3d_{random.randint(1000, 9999)}.png"
        img.save(filename)
        
        print(f"🎨 [Image Generated] Local 3D Graphics Canvas Render Complete in {(time.time()-start)*1000:.2f}ms")
        
        return {
            "status": "Success",
            "file": filename,
            "style": "3D_Mathematical_Grid_Graphics",
            "reply": f"Maine local mathematical synthesis se grids aur realistic 3D vibrant colours ke sath graphic canvas tayaar karke save kar diya hai: {filename}"
        }

    # --- IMAGE PARAKH / ANALYSIS ENGINE ---
    def analyze_visual_data(self, image_obj):
        """ Deep Image Data Hashing Loop """
        try:
            img_rgb = image_obj.convert("RGB")
            pixels = list(img_rgb.getdata())
            sample_size = min(len(pixels), 1500)
            sampled = random.sample(pixels, sample_size)
            
            avg_r = sum(p[0] for p in sampled) / sample_size
            avg_g = sum(p[1] for p in sampled) / sample_size
            avg_b = sum(p[2] for p in sampled) / sample_size
            
            img_hash = round(abs(math.sin(avg_r) * math.cos(avg_g) * math.pi) % 1, 8)
            features = {
                "status": "Success",
                "visual_pi_hash": img_hash,
                "dominant_color": f"R:{int(avg_r)} G:{int(avg_g)} B:{int(avg_b)}",
                "message": "Image Matrix Processed Privately."
            }
            self.visual_memory[img_hash] = features
            self.tatkal_grahanam("Visual_Eye_Feed", f"Processed uploaded image with colors R:{int(avg_r)} G:{int(avg_g)}")
            return features
        except Exception as e:
            return {"status": "Failed", "error": str(e)}
