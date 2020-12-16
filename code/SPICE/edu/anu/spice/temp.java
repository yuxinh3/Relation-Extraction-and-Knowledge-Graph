package json;
 
import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import org.json.JSONException;
import org.json.JSONObject;
import org.json.JSONArray;
 
public class JsonConvert {
 
	/**
	 * @param args
	 */
	public static void main(String[] args) {
		// 读取nameID.txt文件中的NAMEID字段（key）对应值（value）并存储
		ArrayList<String> list = new ArrayList<String>();
		BufferedReader brname;
		try {
			brname = new BufferedReader(new FileReader("src/json/nameID.txt"));// 读取NAMEID对应值
			String sname = null;
			while ((sname = brname.readLine()) != null) {
				// System.out.println(sname);
				list.add(sname);// 将对应value添加到链表存储
			}
			brname.close();
		} catch (IOException e1) {
			// TODO Auto-generated catch block
			e1.printStackTrace();
		}
		// 读取原始json文件并进行操作和输出
		try {
			BufferedReader br = new BufferedReader(new FileReader(
					"src/json/HK_geo.json"));// 读取原始json文件
			BufferedWriter bw = new BufferedWriter(new FileWriter(
					"src/json/HK_new.json"));// 输出新的json文件
			String s = null, ws = null;
			while ((s = br.readLine()) != null) {
				// System.out.println(s);
				try {
					JSONObject dataJson = new JSONObject(s);// 创建一个包含原始json串的json对象
					JSONArray features = dataJson.getJSONArray("features");// 找到features的json数组
					for (int i = 0; i < features.length(); i++) {
						JSONObject info = features.getJSONObject(i);// 获取features数组的第i个json对象
						JSONObject properties = info.getJSONObject("properties");// 找到properties的json对象
						String name = properties.getString("name");// 读取properties对象里的name字段值
						System.out.println(name);
						properties.put("NAMEID", list.get(i));// 添加NAMEID字段
						// properties.append("name", list.get(i));
						System.out.println(properties.getString("NAMEID"));
						properties.remove("ISO");// 删除ISO字段
					}
					ws = dataJson.toString();
					System.out.println(ws);
				} catch (JSONException e) {
					// TODO Auto-generated catch block
					e.printStackTrace();
				}
			}
 
			bw.write(ws);
			// bw.newLine();
 
			bw.flush();
			br.close();
			bw.close();
 
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 
	}
 
}