package main;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.ArrayList;

public class BasicScraper {
	
	private String errorMessage;

	
	public BasicScraper(){
		this.errorMessage = "No Error";
	};
	
	
	public String getErrorMessage(){
		return this.errorMessage;
	}
	
	private void resetErrorMessage(){
		this.errorMessage = "No Error";
	}
	
	public URL getPage(String url){
		URL page = null;
		
		resetErrorMessage();
		
		try{
			page = new URL(url);
		} catch(MalformedURLException e){
			System.out.println(e.getMessage());
		}
	
		
		if(page == null){
			this.errorMessage = "Failed to Resolve Page";
			System.out.println(errorMessage);
		}
		
		System.out.println(page.toString());
		return page;
	}
	
	public ArrayList<String> getSourceLinesWithString(URL page, String key){
		ArrayList<String> targetList = new ArrayList<String>();
		
		resetErrorMessage();
		
		try{
			BufferedReader pageReader = new BufferedReader(
			        new InputStreamReader(page.openStream()));
			String sourceLine = pageReader.readLine();
			while(sourceLine != null){
				if(sourceLine.contains(key)){
					targetList.add(sourceLine);
				}
				sourceLine = pageReader.readLine();
			}
			
		} catch (IOException e){
			System.out.println(e.getMessage());
		}
		
		if(targetList.isEmpty()){
			this.errorMessage = "No Line in "+ page.getPath() + " with \"" + key + "\"";
		}
		
		return targetList;
	}
	
	public ArrayList<String> getSourceLinesList(URL page){
		ArrayList<String> lineArray = new ArrayList<>();
		
		resetErrorMessage();
		
		try{
			BufferedReader pageReader = new BufferedReader(
			        new InputStreamReader(page.openStream()));
			String sourceLine = pageReader.readLine();
			while(sourceLine != null){
				lineArray.add(sourceLine);
				sourceLine = pageReader.readLine();
			}
			
		} catch (IOException e){
			System.out.println(e.getMessage());
		}
		
		if(lineArray.isEmpty()){
			this.errorMessage = "No Lines in "+ page.getPath();
		}
		
		return lineArray;
	}
	

}
