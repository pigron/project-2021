FROM node:lts-alpine as build-stage
RUN npm install -g http-server
WORKDIR /app
COPY package*.json ./
RUN npm install --production
COPY . .
RUN npm install vue
RUN npm run build
EXPOSE 8080

FROM nginx:stable-alpine as production-stage
COPY --from=build-stage /app/dist /usr/share/nginx/html
COPY ./default.conf /etc/nginx/conf.d/default.conf
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]