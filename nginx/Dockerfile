FROM nginx:1.25.4-alpine

RUN rm -rf /etc/nginx/conf.d/* \
 && rm -rf /var/cache/apk/*

COPY ./nginx.conf /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]