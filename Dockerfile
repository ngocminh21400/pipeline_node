FROM node:slim
WORKDIR /usr/src/app
ENV WELCOM_MESSAGE="Hello From Ming Ming"
COPY package.json .
COPY yarn.lock .
RUN npm install
COPY index.js .
EXPOSE 4000
CMD ["node","index"]