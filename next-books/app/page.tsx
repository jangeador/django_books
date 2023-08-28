import Image from "next/image";

interface Book {
    title: string;
    pages: number;
    author: { name: string };
    country: string;
    language: string;
    image_link: string;
    year: string;
    link: string;
}

export default async function Home() {

    const getBooks = async () => {
        const res = await fetch('http://127.0.0.1:8000/api/v1/books/', {
            headers: {"Content-type": "application/json"}
        })
        return await res.json()
    }

    const books = await getBooks()

    return (
        <section className="p-4">
            <h1 className="text-xl pb-3">Books</h1>

            {books.map((book: Book, index: number) => (
                <div key={index} className="py-3 flex gap-2">
                    <Image src={`/${book.image_link}`} alt={book.title}
                    width={60} height={60}></Image>
                    <div>
                        <p className="font-bold">{book.title}</p>
                        <p className="text-sm">{book.author.name}</p>
                    </div>

                </div>
            ))}

        </section>
    )
}
