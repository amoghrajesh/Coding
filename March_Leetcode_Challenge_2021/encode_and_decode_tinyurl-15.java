public class Codec {
    HashMap<String, String> longToShort = new HashMap<String, String>();
    HashMap<String, String> shortToLong = new HashMap<String, String>();
    String seed = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ";
    int nextid = 0;
    // Encodes a URL to a shortened URL.
    public String encode(String longUrl) {
        if (longToShort.containsKey(longUrl)) {
            return longToShort.get(longUrl);
        }
        StringBuilder sb = new StringBuilder();
        int id = nextid;
        for (int i = 0; i < 6; i ++) {
            int j = id % 62;
            id = id / 62;
            sb.insert(0, seed.charAt(j));
        }
        String res = sb.toString();
        shortToLong.put(res, longUrl);
        longToShort.put(longUrl, res);
        nextid ++;
        return res;
    }

    // Decodes a shortened URL to its original URL.
    public String decode(String shortUrl) {
        if (!shortToLong.containsKey(shortUrl)) {
            return null;
        }
        return shortToLong.get(shortUrl);
    }
}
