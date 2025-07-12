import React, { useState } from "react";

function App() {
  const [url, setUrl] = useState("");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");
  const [success, setSuccess] = useState("");

  const handleDownload = async (e) => {
    e.preventDefault();
    setLoading(true);
    setError("");
    setSuccess("");
    
    try {
      const response = await fetch("http://localhost:5000/download", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url: url.trim() }),
      });

      if (!response.ok) {
        const err = await response.json();
        setError(err.error || "Xatolik yuz berdi");
        setLoading(false);
        return;
      }

      const blob = await response.blob();
      const downloadUrl = window.URL.createObjectURL(blob);
      const a = document.createElement("a");
      a.href = downloadUrl;
      a.download = "audio.mp3";
      document.body.appendChild(a);
      a.click();
      a.remove();
      window.URL.revokeObjectURL(downloadUrl);
      
      setSuccess("Audio muvaffaqiyatli yuklandi!");
      setUrl("");
      setLoading(false);
    } catch (err) {
      setError("Tarmoq xatosi yoki server ishlamayapti");
      setLoading(false);
    }
  };

  const clearMessages = () => {
    setError("");
    setSuccess("");
  };

  return (
    <div style={{ 
      maxWidth: 600, 
      margin: "50px auto", 
      padding: 30, 
      border: "1px solid #e0e0e0", 
      borderRadius: 15,
      boxShadow: "0 4px 20px rgba(0,0,0,0.1)",
      backgroundColor: "#fff"
    }}>
      <div style={{ textAlign: "center", marginBottom: 30 }}>
        <h1 style={{ 
          color: "#1976d2", 
          marginBottom: 10,
          fontSize: "2.5rem",
          fontWeight: "bold"
        }}>
          🎵 Audio Yuklovchi
        </h1>
        <p style={{ 
          color: "#666", 
          fontSize: "1.1rem",
          marginBottom: 20
        }}>
          YouTube, Instagram, X, Pinterest, Threads dan audio yuklab oling
        </p>
      </div>

      <form onSubmit={handleDownload}>
        <div style={{ marginBottom: 20 }}>
          <input
            type="text"
            placeholder="YouTube, Instagram, X, Pinterest, Threads linkini kiriting..."
            value={url}
            onChange={(e) => {
              setUrl(e.target.value);
              clearMessages();
            }}
            style={{ 
              width: "100%", 
              padding: 15, 
              fontSize: "1rem",
              border: "2px solid #e0e0e0", 
              borderRadius: 10,
              outline: "none",
              transition: "border-color 0.3s"
            }}
            onFocus={(e) => e.target.style.borderColor = "#1976d2"}
            onBlur={(e) => e.target.style.borderColor = "#e0e0e0"}
            required
            disabled={loading}
          />
        </div>
        
        <button
          type="submit"
          style={{ 
            width: "100%", 
            padding: 15, 
            background: loading ? "#ccc" : "#1976d2", 
            color: "#fff", 
            border: "none", 
            borderRadius: 10,
            fontSize: "1.1rem",
            fontWeight: "bold",
            cursor: loading ? "not-allowed" : "pointer",
            transition: "background-color 0.3s"
          }}
          disabled={loading}
        >
          {loading ? "⏳ Yuklanmoqda..." : "⬇️ Yuklab olish"}
        </button>
      </form>

      {error && (
        <div style={{ 
          color: "#d32f2f", 
          marginTop: 20, 
          padding: 15,
          backgroundColor: "#ffebee",
          borderRadius: 8,
          border: "1px solid #ffcdd2"
        }}>
          <strong>Xatolik:</strong> {error}
        </div>
      )}

      {success && (
        <div style={{ 
          color: "#2e7d32", 
          marginTop: 20, 
          padding: 15,
          backgroundColor: "#e8f5e8",
          borderRadius: 8,
          border: "1px solid #c8e6c9"
        }}>
          <strong>Muvaffaqiyatli!</strong> {success}
        </div>
      )}

      <div style={{ 
        marginTop: 30, 
        padding: 20,
        backgroundColor: "#f5f5f5",
        borderRadius: 10,
        color: "#666"
      }}>
        <h3 style={{ color: "#1976d2", marginBottom: 15 }}>📋 Qo'llab-quvvatlanadi:</h3>
        <ul style={{ 
          listStyle: "none", 
          padding: 0,
          display: "grid",
          gridTemplateColumns: "repeat(auto-fit, minmax(150px, 1fr))",
          gap: 10
        }}>
          <li style={{ padding: "8px 0" }}>🎥 YouTube</li>
          <li style={{ padding: "8px 0" }}>📸 Instagram</li>
          <li style={{ padding: "8px 0" }}>🐦 X (Twitter)</li>
          <li style={{ padding: "8px 0" }}>📌 Pinterest</li>
          <li style={{ padding: "8px 0" }}>🧵 Threads</li>
        </ul>
      </div>

      <div style={{ 
        marginTop: 20, 
        textAlign: "center",
        color: "#999",
        fontSize: "0.9rem"
      }}>
        <p>⚠️ Faqat shaxsiy foydalanish uchun. Mualliflik huquqlariga hurmat bering.</p>
      </div>
    </div>
  );
}

export default App; 