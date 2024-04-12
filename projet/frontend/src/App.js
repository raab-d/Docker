/*import React from 'react';
import './App.css';
import PostForm from './components/PostForm';


function App() {
  return (
    <div className="App">
      <header className="App-header">
        <p>
          **Edit <code>src/App.js</code> and save to reload.
        </p>
      </header>
    </div>
  );
}

export default App;
*/
import React, { useEffect, useState } from 'react';
import './App.css';
import PostForm from './components/PostForm';

function App() {
  const [posts, setPosts] = useState([]);
  const [editingPost, setEditingPost] = useState(null);

  useEffect(() => {
    // Simuler le chargement des posts
    const loadPosts = async () => {
      const response = await fetch('http://localhost:5000/posts');
      const data = await response.json();
      setPosts(data);
    };
    loadPosts();
  }, []);

  const startEditing = (post) => {
    setEditingPost(post);
  };

  const savePost = async (post) => {
    // Déterminer si le post existe déjà (mise à jour) ou s'il s'agit d'un nouveau post (ajout)
    const method = post.id ? 'PUT' : 'POST'; // Utilisez 'PUT' pour une mise à jour et 'POST' pour créer
    const url = `http://backend:5000/posts${post.id ? '/' + post.id : ''}`; // Ajoutez l'ID du post dans l'URL pour les mises à jour
  
    const response = await fetch(url, {
      method: method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(post)
    });
  
    const newPost = await response.json();
  
    if (method === 'POST') {
      setPosts([...posts, newPost.post]); // Ajout du nouveau post à la liste
    } else {
      const updatedPosts = posts.map(p => p.id === post.id ? newPost.post : p); // Mise à jour du post dans la liste
      setPosts(updatedPosts);
    }
    setEditingPost(null); // Réinitialiser le post en cours d'édition
  };
  
  return (
    <div className="App">
      {editingPost ? (
        <PostForm post={editingPost} onSave={savePost} />
      ) : (
        <PostForm onSave={savePost} />
      )}
      {posts.map(post => (
        <div key={post.id}>
          <h3>{post.title}</h3>
          <p>{post.content}</p>
          <button onClick={() => startEditing(post)}>Edit</button>
        </div>
      ))}
    </div>
  );
}

export default App;
