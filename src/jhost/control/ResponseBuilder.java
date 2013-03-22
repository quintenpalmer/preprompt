package control;

public class ResponseBuilder{

	public String respondTest(int version){
		String resp = "<resp>";
		resp += "<resp_status>ok</resp_status>";
		resp += "<resp_type>test</resp_type>";
		resp += "<version>"+Integer.toString(version)+"</version>";
		resp += "</resp>";
		return resp;
	}

	public String respondExit(){
		String resp = "<resp>";
		resp += "<resp_status>ok</resp_status>";
		resp += "<resp_type>exit</resp_type>";
		resp += "</resp>";
		return resp;
	}

	public String respondNotImplemented(){
		String resp = "<resp>";
		resp += "<resp_status>ok</resp_status>";
		resp += "<resp_type>noexist</resp_type>";
		resp += "</resp>";
		return resp;
	}

	public String respondError(String errorMessage){
		String resp = "<resp>";
		resp += "<resp_status>ok</resp_status>";
		resp += "<resp_type>error</resp_type>";
		resp += "<error_message>"+errorMessage+"</error_message>";
		resp += "</resp>";
		return resp;
	}
}
