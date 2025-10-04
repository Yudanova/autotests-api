This project demonstrates a simple gRPC API for retrieving course information. It includes:

- ✅ Protocol Buffers contract (`.proto`)
- ✅ gRPC server implementation
- ✅ gRPC client implementation
- ✅ Auto-generated Python bindings

🚀 How to run the server

Start the gRPC server:
python -m grpc_course_server

Expected output:
gRPC server started on port 50051...

📡 How to run the client

In a separate terminal:
python -m grpc_course_client

Expected output:
course_id: "api-course"
title: "Autotests API"
description: "Learning API autotests"

📦 Example RPC Flow
- Request: GetCourseRequest(course_id="api-course")
- Response:
{
  "course_id": "api-course",
  "title": "Autotests API",
  "description": "Learning API autotests"
}

🧪 Testing Idea using unittest or pytest
Example:
def test_get_course():
    servicer = CourseServiceServicer()
    request = GetCourseRequest(course_id="test-id")
    response = servicer.GetCourse(request, None)
    assert response.title == "Autotests API"

📌 Notes for this simple project, just for learning
- This project uses Protocol Buffers for efficient serialization.
- Communication is done over HTTP/2 using gRPC.
- Ideal for learning how to build fast, scalable APIs.

________________________

To run local server for tests:
Open project: qa-automation-engineer-api-course

Run:
uvicorn main:app --reload

Open: http://localhost:8000
And:  http://localhost:8000/docs

Expected: Both urls should be opened, readable and usable