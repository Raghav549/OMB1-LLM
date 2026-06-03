import com.sun.net.httpserver.HttpServer;
import java.io.*;
import java.net.InetSocketAddress;

public class OMB1Api {
    private static final OMB1Brain brain = new OMB1Brain();

    public static void main(String[] args) throws IOException {
        int port = System.getenv("PORT") != null ? Integer.parseInt(System.getenv("PORT")) : 8080;
        HttpServer server = HttpServer.create(new InetSocketAddress(port), 0);

        server.createContext("/api/chat", exchange -> {
            exchange.getResponseHeaders().add("Access-Control-Allow-Origin", "*");
            String resp = "{\"reply\": \"" + brain.query("test") + "\"}";
            exchange.sendResponseHeaders(200, resp.length());
            try (OutputStream os = exchange.getResponseBody()) { os.write(resp.getBytes()); }
        });

        server.start();
        System.out.println("OMB1 Java 26 Power Engine Online on port " + port);
    }
}
