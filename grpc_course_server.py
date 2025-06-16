from concurrent import futures
import grpc

import course_service_pb2
import course_service_pb2_grpc


class CourseServiceServicer(course_service_pb2_grpc.CourseServiceServicer):
    """Реализация методов gRPC-сервиса CourseService"""

    def GetCourse(self, request, context):
        print(f"🔥 Запрос получен: {request.course_id}")
        return course_service_pb2.GetCourseResponse(
            course_id=request.course_id,
            title="Автотесты API",
            description="Будем изучать написание API автотестов"
        )


def serve():
    """Создание и запуск gRPC-сервера"""
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    course_service_pb2_grpc.add_CourseServiceServicer_to_server(CourseServiceServicer(), server)

    # Диагностика: выводим зарегистрированные сервисы и методы
    print("Зарегистрированные сервисы и методы:")
    for service_name, service in course_service_pb2.DESCRIPTOR.services_by_name.items():
        print(f"Сервис: {service_name}")
        for method in service.methods:
            print(f"Метод: {method.name}")

    server.add_insecure_port('[::]:50051')
    server.start()
    print("gRPC сервер запущен на порту 50051...")
    server.wait_for_termination()


if __name__ == "__main__":
    serve()
