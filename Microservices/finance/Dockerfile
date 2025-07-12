FROM eclipse-temurin:17-jdk-alpine

WORKDIR /app

RUN apk add --no-cache maven

# Copy pom.xml only
COPY source_code/pom.xml .

# Copy source code
COPY source_code/src ./src

RUN mvn clean package -DskipTests

CMD ["java", "-jar", "target/finance-0.0.1-SNAPSHOT.jar"]
