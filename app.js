const express = require('express');
const mongoose = require('mongoose');
const bodyParser = require('body-parser');

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(bodyParser.json());

// Connect to MongoDB
mongoose.connect('mongodb://localhost:27017/notesDB', {
    useNewUrlParser: true,
    useUnifiedTopology: true
}).then(() => console.log('MongoDB Connected'))
  .catch(err => console.log(err));

// Note Schema
const noteSchema = new mongoose.Schema({
    title: String,
    content: String
});

const Note = mongoose.model('Note', noteSchema);

// Routes
app.get('/notes', async (req, res) => {
    const notes = await Note.find();
    res.json(notes);
});

app.post('/notes', async (req, res) => {
    const { title, content } = req.body;
    const newNote = new Note({ title, content });
    await newNote.save();
    res.json(newNote);
});

app.put('/notes/:id', async (req, res) => {
    const { title, content } = req.body;
    const updatedNote = await Note.findByIdAndUpdate(req.params.id, { title, content }, { new: true });
    res.json(updatedNote);
});

app.delete('/notes/:id', async (req, res) => {
    await Note.findByIdAndDelete(req.params.id);
    res.json({ message: 'Note deleted' });
});

// Start server
app.listen(PORT, () => console.log(`Server running on port ${PORT}`));
