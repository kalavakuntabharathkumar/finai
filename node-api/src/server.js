import express from 'express';
import cors from 'cors';

const app = express();
const port = process.env.PORT || 3001;
app.use(cors({ origin: 'http://localhost:5173' }));
app.use(express.json({ limit: '1mb' }));

const events = [
  { id: 'EVT-101', type: 'reconciliation.completed', description: 'Daily cash reconciliation finished', status: 'Resolved', time: '09:42 AM' },
  { id: 'EVT-102', type: 'variance.flagged', description: 'Unusual expense variance flagged for review', status: 'Review', time: '09:18 AM' },
  { id: 'EVT-103', type: 'invoice.duplicate_check', description: 'Duplicate invoice check completed', status: 'Resolved', time: '08:56 AM' }
];

app.get('/health', (_req, res) => res.json({ status: 'UP', service: 'financial-insights-api' }));
app.get('/api/insights', (_req, res) => res.json({
  metrics: { queries: 1284, deflectionRate: 35, medianResponseSeconds: 4.2 },
  events
}));
app.post('/api/events', (req, res) => {
  const { type, description } = req.body ?? {};
  if (typeof type !== 'string' || typeof description !== 'string' || !type.trim() || !description.trim()) {
    return res.status(400).json({ error: 'type and description are required strings' });
  }
  const event = { id: `EVT-${Date.now()}`, type: type.trim(), description: description.trim(),
    status: 'Review', time: new Date().toLocaleTimeString('en-US', { hour: '2-digit', minute: '2-digit' }) };
  events.unshift(event);
  res.status(201).json(event);
});

app.listen(port, () => console.log(`Financial insights API listening on ${port}`));
export { app };
