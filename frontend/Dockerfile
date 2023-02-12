# syntax=docker/dockerfile:1

# build stage
FROM node:lts-alpine as hd-front-build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# production stage
FROM nginx:stable-alpine as phd-front-roduction-stage
COPY --from=hd-front-build-stage /app/dist /usr/share/nginx/html
EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]