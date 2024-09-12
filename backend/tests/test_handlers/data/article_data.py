all_types = {
    "title": "string",
    "content": [
        {
            "id": "string",
            "type": "paragraph",
            "level": 0,
            "value": "string",
            "children": [
                {
                    "id": "string",
                    "type": "string",
                    "text": "string",
                    "href": "string",
                    "attributes": {},
                    "description": "string",
                }
            ],
        },
        {
            "id": "string",
            "type": "video",
            "children": [
                {
                "src": "string",
                "mimeType": "string",
                "text": "string"
                }
            ]
        },
        {"id": "string", "type": "file", "href": "string", "download": "string"},
        {
            "id": "string",
            "type": "test",
            "isRetaking": True,
            "images": ["string"],
            "children": [
                {
                    "id": "string",
                    "type": "string",
                    "text": "string",
                    "href": "string",
                    "attributes": {},
                    "description": "string",
                }
            ],
            "selection": "string",
            "options": [{"id": "string", "title": "text", "comment": "string"}],
            "answer": "string",
        },
    ],
}

one_type = {
    "title": "string",
    "content": [
        {
            "id": "string",
            "type": "paragraph",
            "value": "string",
            "level": 0,
            "children": [
                {
                    "id": "string",
                    "type": "string",
                    "text": "string",
                    "href": "string",
                    "attributes": {},
                    "description": "string",
                }
            ],
        }
    ],
}

bad_article = {
    "title": "string",
    "content": [
        {
            "id": "string",
            "type": "paragraph",
            "level": 0,
            "value": "string",
            "children": [
                {
                    "id": "string",
                }
            ],
        }
    ],
}
