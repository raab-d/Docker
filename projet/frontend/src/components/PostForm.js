import React, { useState, useEffect } from 'react';

function PostForm({ post, onSave }) {
    const [title, setTitle] = useState('');
    const [content, setContent] = useState('');
    const [message, setMessage] = useState(''); // État pour stocker le message de retour

    // Lorsque le post en édition change, mettre à jour les champs de formulaire
    useEffect(() => {
        if (post) {
            setTitle(post.title);
            setContent(post.content);
            setMessage(''); // Réinitialiser le message lors du chargement d'un nouveau post pour édition
        }
    }, [post]);

    const handleSubmit = async (e) => {
        e.preventDefault();
        const newPost = { title, content, id: post ? post.id : undefined };
        try {
            const response = await fetch('http://localhost:5000/posts', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify(newPost)
            });
            const result = await response.json();
            if (response.ok) {
                onSave(newPost); // Utilisation du callback onSave pour sauvegarder
                setTitle('');
                setContent('');
                setMessage('Post créé avec succès !'); // Afficher un message de succès
            } else {
                setMessage('Échec de la création du post.'); // Afficher un message d'erreur
            }
        } catch (error) {
            console.error('Erreur:', error);
            setMessage('Erreur lors de la création du post.'); // Afficher un message d'erreur en cas d'exception
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <label>
                Title:
                <input
                    type="text"
                    value={title}
                    onChange={(e) => setTitle(e.target.value)}
                />
            </label>
            <label>
                Content:
                <textarea
                    value={content}
                    onChange={(e) => setContent(e.target.value)}
                />
            </label>
            <button type="submit">{post ? 'Update' : 'Save'}</button>
            {message && <p>{message}</p>} // Affichage du message
        </form>
    );
}

export default PostForm;
