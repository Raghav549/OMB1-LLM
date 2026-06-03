import java.util.concurrent.*;
import java.sql.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import javax.imageio.ImageIO;
import org.apache.tika.Tika;
import java.io.File;

public class OMB1Brain {
    private final ExecutorService executor = Executors.newVirtualThreadPerTaskExecutor();
    private final String DB = "omb1_infinity.db";

    public OMB1Brain() {
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:" + DB)) {
            conn.createStatement().execute("CREATE TABLE IF NOT EXISTS matrix (hash REAL PRIMARY KEY, content TEXT, dtype TEXT)");
        } catch (Exception e) { e.printStackTrace(); }
    }

    // Features: Instant Ingestion (File to Text)
    public String ingestFile(String path) {
        return new Tika().parseToString(new File(path));
    }

    // Features: Visual Engine (Art generation)
    public void generateArt(String prompt) throws Exception {
        BufferedImage img = new BufferedImage(500, 500, BufferedImage.TYPE_INT_RGB);
        Graphics2D g = img.createGraphics();
        g.setColor(Color.BLACK); g.fillRect(0,0,500,500);
        g.setColor(Color.GREEN); g.drawString("OMB1 AI: " + prompt, 50, 250);
        g.dispose();
        ImageIO.write(img, "png", new File("art.png"));
    }

    public void train(String in, String data, String type) {
        executor.submit(() -> {
            double h = Math.abs(in.hashCode() * Math.PI) % 1.0;
            try (Connection conn = DriverManager.getConnection("jdbc:sqlite:" + DB);
                 PreparedStatement ps = conn.prepareStatement("INSERT OR REPLACE INTO matrix VALUES (?,?,?)")) {
                ps.setDouble(1, h); ps.setString(2, data); ps.setString(3, type); ps.executeUpdate();
            } catch (SQLException e) { e.printStackTrace(); }
        });
    }

    public String query(String input) {
        double h = Math.abs(input.hashCode() * Math.PI) % 1.0;
        try (Connection conn = DriverManager.getConnection("jdbc:sqlite:" + DB);
             PreparedStatement ps = conn.prepareStatement("SELECT content FROM matrix WHERE hash = ?")) {
            ps.setDouble(1, h); ResultSet rs = ps.executeQuery();
            return rs.next() ? rs.getString("content") : "Info not in Pi-Matrix.";
        } catch (SQLException e) { return "Error"; }
    }
}
