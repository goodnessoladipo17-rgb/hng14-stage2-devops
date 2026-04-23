FROM node:18-slim AS builder
WORKDIR /app
COPY package.json .
RUN npm install --omit=dev

FROM node:18-slim AS runner
WORKDIR /app
RUN useradd --create-home --shell /bin/bash appuser
COPY --from=builder /app/node_modules ./node_modules
COPY . .
USER appuser
ENV PORT=3000
EXPOSE 3000
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD node -e "require('http').get('http://localhost:3000', (r) => r.statusCode === 200 ? process.exit(0) : process.exit(1))"
CMD ["node", "app.js"]