package main;

import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.net.URL;
import java.util.ArrayList;
import java.util.StringTokenizer;


public class Main {

	public static void main(String[] args) throws IOException, InterruptedException {

		BasicScraper scraper = new BasicScraper();
		
		FileWriter writer = new FileWriter(System.getProperty("user.dir") + 
				File.separator + "AntPoolBlockData.csv", true);
		
		for(int pageNum = 1; pageNum < 305; pageNum++){	
		
			Thread.sleep(500);
			
			System.out.println(pageNum);
			
			URL antStatPage = scraper.getPage("https://www.antpool.com/poolStats.htm?tp=" + pageNum);
			
			ArrayList<String> tableLines = scraper.getSourceLinesWithString(antStatPage, "<td class=");
			
			ArrayList<String> pageData = new ArrayList<>();
			
			for(String line : tableLines){
				StringTokenizer tokens = new StringTokenizer(line, ">");
				while(tokens.hasMoreTokens()){
					String next = tokens.nextToken();
					int stop = next.indexOf("<");
					char first = next.charAt(0);
					if(first >= '0' && first <= '9' && stop > -1){
						String data = next.substring(0, stop);
						data = data.replace(",", "");
						if(data.indexOf(";") != -1){
							data = data.substring(0, data.length()-7);
						}
						pageData.add(data);
					}
				}
			}
			
			ArrayList<String> dataRows = new ArrayList<>();
	
			int i = 0;
			while(i < pageData.size()){
				String dataRow = pageData.get(i);
				i++;
				while(i < pageData.size() &&
						!(pageData.get(i).length() == 6 && 
						pageData.get(i).charAt(5) >= '0' &&
						pageData.get(i).charAt(5) <= '9')){
					dataRow += "," + pageData.get(i);
					i++;
				}
				dataRows.add(dataRow);
			}
			
			for(String row : dataRows){
				writer.write(row);
				writer.write(System.getProperty("line.separator"));
				System.out.println(row);
			}
		
		}
		
		writer.close();
		
	}

}
