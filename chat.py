import customtkinter as ctk
import tkinter as tk
from PIL import Image, ImageTk
from datetime import datetime

class ShoppingChatBot:
    def __init__(self):
        # Konfigurasi tema yang lebih modern
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Buat window utama dengan ikon dan styling
        self.root = ctk.CTk()
        self.root.title("🔫 GunBot - Toko Senjata Online")
        self.root.geometry("700x800")
        self.root.minsize(600, 700)
        self.root.configure(fg_color="#1a1a1a")
        
        # Data produk yang diperluas
        self.products = {
            "Senjata laras panjang": {
                "items": ["Sniper Alpha", "Precision X9", "Long Range Elite"],
                "icon": "🎯"
            },
            "Senjata defender": {
                "items": ["Taktis X-15", "Defender P900", "Taurus Judge Defender", "Shotgun Defender S12"],
                "icon": "🛡️"
            },
            "Senjata serbu": {
                "items": ["Serbu AR-2030", "Assault Pro", "Combat X7"],
                "icon": "⚔️"
            },
            "Senjata melee": {
                "items": ["Karambit Shadow", "Golok Pranjurit", "Combat Knife Pro"],
                "icon": "🔪"
            },
            "Granat & Bom": {
                "items": ["Granat Asap M18", "Flashbang X2", "Tactical Grenade"],
                "icon": "💣"
            },
            "Aksesoris": {
                "items": ["Red Dot Sight", "Tactical Grip", "Extended Magazine", "Silencer Pro"],
                "icon": "🔧"
            }
        }
        
        self.prices = {
            "Sniper Alpha": "Rp 25.000.000",
            "Precision X9": "Rp 28.500.000",
            "Long Range Elite": "Rp 32.000.000",
            "Taktis X-15": "Rp 2.400.000",
            "Defender P900": "Rp 4.200.000",
            "Taurus Judge Defender": "Rp 6.500.000",
            "Shotgun Defender S12": "Rp 7.800.000",
            "Serbu AR-2030": "Rp 18.000.000",
            "Assault Pro": "Rp 21.000.000",
            "Combat X7": "Rp 19.500.000",
            "Karambit Shadow": "Rp 900.000",
            "Golok Pranjurit": "Rp 1.200.000",
            "Combat Knife Pro": "Rp 1.500.000",
            "Granat Asap M18": "Rp 750.000",
            "Flashbang X2": "Rp 850.000",
            "Tactical Grenade": "Rp 950.000"
        }
        
        self.quick_questions = [
            "Kategori senjata apa saja?",
            "Tampilkan semua produk!",
            "Harga senjata laras panjang?",
            "Cara pembayaran?",
            "Ada promo saat ini?",
            "Waktu pengiriman?",
            "Bantu saya memilih",
            "Produk legal & berkualitas?"
        ]
        
        # Warna tema
        self.colors = {
            "primary": "#2E86AB",
            "secondary": "#A8D0E6",
            "accent": "#F76C6C",
            "dark_bg": "#1a1a1a",
            "light_bg": "#2d2d2d",
            "text_light": "#ffffff",
            "text_dark": "#cccccc"
        }
        
        self.setup_ui()
        
    def setup_ui(self):
        # Configure grid untuk responsive layout
        self.root.grid_rowconfigure(1, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # HEADER dengan gradient effect
        header_frame = ctk.CTkFrame(
            self.root, 
            height=100, 
            fg_color=self.colors["primary"],
            corner_radius=0
        )
        header_frame.grid(row=0, column=0, sticky="ew", padx=0, pady=0)
        header_frame.grid_propagate(False)
        
        # Header content dengan icon dan title
        header_content = ctk.CTkFrame(header_frame, fg_color="transparent")
        header_content.pack(expand=True, fill="both", padx=20)
        
        title_label = ctk.CTkLabel(
            header_content, 
            text="🔫 GUNBOT - Toko Senjata Online",
            font=("Arial", 22, "bold"),
            text_color="white"
        )
        title_label.pack(side="left", pady=20)
        
        status_label = ctk.CTkLabel(
            header_content,
            text="🟢 Online",
            font=("Arial", 12),
            text_color="#00ff00"
        )
        status_label.pack(side="right", pady=20)
        
        # CHAT AREA dengan styling modern
        self.chat_frame = ctk.CTkScrollableFrame(
            self.root, 
            height=400,
            fg_color=self.colors["dark_bg"],
            border_width=0,
            scrollbar_button_color=self.colors["primary"],
            scrollbar_button_hover_color=self.colors["secondary"]
        )
        self.chat_frame.grid(row=1, column=0, sticky="nsew", padx=15, pady=10)
        
        # QUICK QUESTIONS dengan card style
        questions_frame = ctk.CTkFrame(
            self.root, 
            height=140,
            fg_color=self.colors["light_bg"],
            border_width=1,
            border_color="#444444",
            corner_radius=15
        )
        questions_frame.grid(row=2, column=0, sticky="ew", padx=15, pady=5)
        questions_frame.grid_propagate(False)
        
        questions_label = ctk.CTkLabel(
            questions_frame, 
            text="💡 Pertanyaan Cepat:",
            font=("Arial", 14, "bold"),
            text_color=self.colors["secondary"]
        )
        questions_label.pack(anchor="w", padx=15, pady=8)
        
        # Container untuk tombol pertanyaan dengan scroll horizontal
        questions_container = ctk.CTkScrollableFrame(
            questions_frame, 
            fg_color="transparent",
            orientation="horizontal",
            height=60
        )
        questions_container.pack(fill="both", expand=True, padx=10, pady=5)
        
        for question in self.quick_questions:
            btn = ctk.CTkButton(
                questions_container,
                text=question,
                font=("Arial", 11),
                height=35,
                fg_color=self.colors["primary"],
                hover_color=self.colors["secondary"],
                text_color="white",
                corner_radius=20,
                border_width=1,
                border_color="#444444",
                command=lambda q=question: self.send_quick_question(q)
            )
            btn.pack(side="left", padx=3, pady=5)
        
        # INPUT AREA dengan styling modern
        input_frame = ctk.CTkFrame(
            self.root, 
            height=70,
            fg_color=self.colors["light_bg"],
            corner_radius=15
        )
        input_frame.grid(row=3, column=0, sticky="ew", padx=15, pady=10)
        input_frame.grid_propagate(False)
        
        # Input container
        input_container = ctk.CTkFrame(input_frame, fg_color="transparent")
        input_container.pack(expand=True, fill="both", padx=15, pady=10)
        
        self.input_entry = ctk.CTkEntry(
            input_container,
            placeholder_text="💬 Ketik pesan Anda...",
            font=("Arial", 13),
            height=45,
            border_width=1,
            border_color="#444444",
            fg_color="#333333",
            text_color="white",
            corner_radius=20
        )
        self.input_entry.pack(side="left", fill="x", expand=True, padx=(0, 10))
        self.input_entry.bind("<Return>", lambda e: self.send_message())
        
        send_button = ctk.CTkButton(
            input_container,
            text="Kirim 🚀",
            font=("Arial", 12, "bold"),
            height=45,
            width=100,
            fg_color=self.colors["accent"],
            hover_color="#ff5252",
            text_color="white",
            corner_radius=20,
            command=self.send_message
        )
        send_button.pack(side="right")
        
        # Focus ke input
        self.input_entry.focus()
        
        # Tampilkan pesan welcome
        self.show_welcome_message()
    
    def show_welcome_message(self):
        welcome_text = """🎯 **Halo! Selamat datang di GUNBOT - Toko Senjata Online**

Saya **GunBot**, asisten virtual yang akan membantu Anda berbelanja senjata dengan aman dan terpercaya. 🔫

**Layanan yang tersedia:**
• 🛍️  Melihat kategori produk senjata
• 💰  Informasi harga dan spesifikasi  
• 🎁  Promo dan diskon spesial
• 🚚  Informasi pengiriman
• 🔒  Konsultasi pemilihan produk

Silakan pilih pertanyaan cepat di bawah atau ketik pertanyaan Anda!"""
        
        self.add_message("GunBot", welcome_text, is_bot=True)
    
    def add_message(self, sender, message, is_bot=False):
        message_frame = ctk.CTkFrame(self.chat_frame, fg_color="transparent")
        message_frame.pack(fill="x", padx=5, pady=3)
        
        # Frame untuk bubble chat dengan styling berbeda
        if is_bot:
            bubble_color = self.colors["primary"]
            avatar_text = "🤖"
            sender_name = "GunBot"
        else:
            bubble_color = self.colors["light_bg"]
            avatar_text = "👤"
            sender_name = "Anda"
        
        # Main message container
        main_container = ctk.CTkFrame(message_frame, fg_color="transparent")
        
        if is_bot:
            main_container.pack(anchor="w")
            # Avatar bot
            avatar_frame = ctk.CTkFrame(
                main_container, 
                width=40, 
                height=40, 
                fg_color=bubble_color,
                corner_radius=20
            )
            avatar_frame.pack(side="left", padx=(0, 10))
            avatar_label = ctk.CTkLabel(
                avatar_frame, 
                text=avatar_text,
                font=("Arial", 16),
                text_color="white"
            )
            avatar_label.pack(expand=True)
        else:
            main_container.pack(anchor="e")
        
        # Content frame
        content_frame = ctk.CTkFrame(
            main_container, 
            corner_radius=20,
            fg_color=bubble_color
        )
        
        if is_bot:
            content_frame.pack(side="left", fill="x", expand=True, padx=(0, 50))
        else:
            content_frame.pack(side="right", fill="x", expand=True, padx=(50, 0))
        
        # Header dengan nama dan waktu
        time_now = datetime.now().strftime("%H:%M")
        header_label = ctk.CTkLabel(
            content_frame,
            text=f"{sender_name} • {time_now}",
            font=("Arial", 10, "bold"),
            text_color="#ffffff" if is_bot else self.colors["text_dark"]
        )
        header_label.pack(anchor="w", padx=15, pady=(10, 5))
        
        # Isi pesan
        message_label = ctk.CTkLabel(
            content_frame,
            text=message,
            font=("Arial", 12),
            text_color="white" if is_bot else self.colors["text_light"],
            justify="left",
            wraplength=400
        )
        message_label.pack(anchor="w", padx=15, pady=(0, 12))
        
        # Auto scroll ke bawah
        self.root.after(100, self.scroll_to_bottom)
    
    def scroll_to_bottom(self):
        """Scroll chat ke paling bawah"""
        self.chat_frame._parent_canvas.yview_moveto(1.0)
    
    def send_message(self):
        user_input = self.input_entry.get().strip()
        if not user_input:
            return
            
        self.add_message("Anda", user_input, is_bot=False)
        self.input_entry.delete(0, tk.END)
        
        # Process bot response dengan delay
        self.root.after(500, lambda: self.process_bot_response(user_input))
    
    def send_quick_question(self, question):
        self.add_message("Anda", question, is_bot=False)
        self.root.after(500, lambda: self.process_bot_response(question))
    
    def process_bot_response(self, user_input):
        user_input_lower = user_input.lower()
        response = ""
        
        # Logic responses yang lebih comprehensive
        if any(word in user_input_lower for word in ["kategori", "jenis", "apa saja"]):
            response = self.get_categories_response()
        elif any(word in user_input_lower for word in ["semua", "tampilkan", "semua produk"]):
            response = self.get_all_products_response()
        elif "laras panjang" in user_input_lower:
            response = self.get_category_detail("Senjata laras panjang")
        elif "defender" in user_input_lower:
            response = self.get_category_detail("Senjata defender")
        elif "serbu" in user_input_lower:
            response = self.get_category_detail("Senjata serbu")
        elif "melee" in user_input_lower or "mele" in user_input_lower:
            response = self.get_category_detail("Senjata melee")
        elif "bom" in user_input_lower or "granat" in user_input_lower:
            response = self.get_category_detail("Granat & Bom")
        elif "aksesoris" in user_input_lower:
            response = self.get_category_detail("Aksesoris")
        elif "harga" in user_input_lower:
            response = self.get_price_response(user_input_lower)
        elif any(word in user_input_lower for word in ["pembayaran", "bayar", "metode"]):
            response = self.get_payment_response()
        elif any(word in user_input_lower for word in ["promo", "diskon", "special"]):
            response = self.get_promo_response()
        elif any(word in user_input_lower for word in ["pengiriman", "kirim", "ongkir"]):
            response = self.get_shipping_response()
        elif any(word in user_input_lower for word in ["bantu", "pilih", "rekomendasi"]):
            response = self.get_help_response()
        elif any(word in user_input_lower for word in ["legal", "berkualitas", "aman"]):
            response = self.get_legal_response()
        elif any(word in user_input_lower for word in ["hai", "halo", "hello", "hi"]):
            response = "Halo! 👋 Ada yang bisa saya bantu hari ini? Silakan tanyakan tentang produk senjata kami!"
        else:
            response = self.get_default_response()
        
        self.add_message("GunBot", response, is_bot=True)
    
    def get_categories_response(self):
        categories_text = ""
        for category, info in self.products.items():
            categories_text += f"{info['icon']} **{category}**\n"
        
        return f"""📦 **KATEGORI PRODUK KAMI:**

{categories_text}

💡 *Ketik nama kategori untuk melihat detail produk*"""
    
    def get_all_products_response(self):
        products_text = ""
        for category, info in self.products.items():
            products_text += f"\n{info['icon']} **{category}:**\n"
            for item in info["items"]:
                price = self.prices.get(item, "Hubungi untuk harga")
                products_text += f"   • {item} - {price}\n"
        
        return f"""🛍️ **SEMUA PRODUK:**{products_text}

📞 *Hubungi CS untuk pemesanan dan info detail*"""
    
    def get_category_detail(self, category):
        if category in self.products:
            info = self.products[category]
            products_text = "\n".join([f"• {item} - {self.prices.get(item, 'Hubungi untuk harga')}" 
                                     for item in info["items"]])
            
            return f"""{info['icon']} **{category.upper()}**

{products_text}

💎 *Semua produk berkualitas tinggi dengan garansi resmi*"""
        return "❌ Kategori tidak ditemukan."
    
    def get_price_response(self, user_input):
        for product, price in self.prices.items():
            if product.lower() in user_input:
                return f"""💰 **HARGA {product.upper()}:**

**Harga:** {price}
**Status:** ✅ Tersedia
**Garansi:** 1 Tahun

📞 *Hubungi CS untuk pemesanan dan nego harga*"""
        
        return "❌ Produk tidak ditemukan. Coba sebutkan nama produk seperti: 'Sniper Alpha', 'Karambit Shadow', atau 'Granat Asap'"
    
    def get_payment_response(self):
        return """💳 **METODE PEMBAYARAN:**

• 🏦 Transfer Bank (BCA, Mandiri, BNI, BRI)
• 💳 Kartu Kredit (Visa, MasterCard)
• 📱 E-Wallet (Gopay, OVO, Dana, ShopeePay)
• 💰 COD (Cash on Delivery) - Area Terbatas

🔒 **Pembayaran 100% aman dan terjamin**
📄 Faktur pajak dan dokumentasi lengkap"""
    
    def get_promo_response(self):
        return """🎉 **PROMO SPESIAL BULAN INI!**

🔥 **DISKON 25%** untuk pembelian pertama
🚚 **GRATIS ONGKIR** min. belanja Rp 5.000.000
💳 **CASHBACK 15%** menggunakan e-wallet
🎁 **BUNDLE SPECIAL** senjata + aksesoris

⏰ **Promo berlaku hingga akhir bulan!**
📞 *Hubungi CS untuk klaim promo*"""
    
    def get_shipping_response(self):
        return """🚚 **INFORMASI PENGIRIMAN:**

📍 **Jakarta & Sekitarnya:** 1-2 hari kerja
📍 **Pulau Jawa:** 2-3 hari kerja  
📍 **Luar Jawa:** 3-7 hari kerja
📍 **Same-day delivery** (area tertentu)

🎁 **Gratis ongkir** untuk pembelian di atas Rp 5.000.000!
🔒 **Packaging aman dan discreet**"""
    
    def get_help_response(self):
        return """🤖 **BANTUAN PEMILIHAN PRODUK**

Beri tahu saya kebutuhan Anda:
• 🎯 **Budget** yang tersedia
• 🛡️ **Kategori** produk yang diinginkan
• ⚔️ **Kebutuhan spesifik** (pertahanan, olahraga, koleksi)

**Contoh:** 
'Saya cari senjata defender budget 5 juta'
'Butuh senjata laras panjang untuk olahraga'

Atau pilih kategori produk untuk melihat opsi!"""
    
    def get_legal_response(self):
        return """🔒 **LEGALITAS & KUALITAS**

✅ **SEMUA PRODUK LEGAL** berizin resmi
✅ **Dokumentasi lengkap** dan faktur pajak
✅ **Berkualitas tinggi** dengan standar internasional
✅ **Garansi resmi** 1 tahun
✅ **Pelatihan penggunaan** gratis

🏆 **Toko terpercaya sejak 2010**"""
    
    def get_default_response(self):
        return """🤔 **Maaf, saya belum paham pertanyaannya.**

Coba tanyakan tentang:
• 🛍️ Kategori produk senjata
• 💰 Harga produk tertentu  
• 🎁 Info promo dan diskon
• 💳 Metode pembayaran
• 🚚 Waktu pengiriman
• 🔒 Legalitas produk

**Atau gunakan tombol pertanyaan cepat di bawah!**"""
    
    def run(self):
        self.root.mainloop()

# Jalankan aplikasi
if __name__ == "__main__":
    print("🚀 Starting GunBot - Toko Senjata Online...")
    app = ShoppingChatBot()
    app.run()