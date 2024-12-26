import React, { useState } from 'react';
import { signIn, signOut, useSession, SessionProvider } from 'next-auth/react';

function HomePage(): JSX.Element {
  const { data: session } = useSession();

  const frameworks = [
    { name: 'Hadoop', description: 'Learn distributed storage and MapReduce.' },
    { name: 'Spark', description: 'Discover in-memory parallel computation.' },
    { name: 'Kafka', description: 'Explore distributed event streaming.' },
    { name: 'Flink', description: 'Dive into high-throughput stream processing.' },
  ];

  const [selectedFramework, setSelectedFramework] = useState<string>('');

  // Placeholder function for launching a Python notebook
  const launchLab = () => {
    alert('Launching Python Notebook in a new window (placeholder)');
  };

  return (
    <div className="min-h-screen bg-white text-gray-900 p-8">
      <header className="flex justify-between items-center mb-8">
        <h1 className="text-2xl font-bold">Taiwan Data Engineering Association</h1>
        <div className="flex gap-4">
          {!session && (
            <>
              <button
                onClick={() => signIn('google')}
                className="bg-blue-600 text-white px-4 py-2 rounded hover:bg-blue-700"
              >
                Sign in with Google
              </button>
              <button
                onClick={() => signIn('github')}
                className="bg-gray-800 text-white px-4 py-2 rounded hover:bg-gray-900"
              >
                Sign in with GitHub
              </button>
            </>
          )}
          {session && (
            <>
              <p className="mr-4">Hello, {session.user?.name}</p>
              <button
                onClick={() => signOut()}
                className="bg-red-600 text-white px-4 py-2 rounded hover:bg-red-700"
              >
                Sign out
              </button>
            </>
          )}
        </div>
      </header>

      <section className="mb-8">
        <h2 className="text-xl font-semibold mb-4">Learning Paths</h2>
        <div className="grid grid-cols-1 sm:grid-cols-2 md:grid-cols-4 gap-4">
          {frameworks.map((fw) => (
            <div
              key={fw.name}
              className="border rounded-xl p-4 hover:shadow cursor-pointer"
              onClick={() => setSelectedFramework(fw.name)}
            >
              <h3 className="font-bold mb-2">{fw.name}</h3>
              <p className="text-sm">{fw.description}</p>
            </div>
          ))}
        </div>
      </section>

      {selectedFramework && (
        <section className="mb-8">
          <h2 className="text-xl font-semibold mb-4">Selected Path: {selectedFramework}</h2>
          <div className="mb-4">Here are labs you can try:</div>
          <div className="flex flex-col gap-4">
            <div className="flex items-center gap-4">
              <div className="bg-gray-200 border-2 border-dashed rounded-xl w-16 h-16" />
              <div>
                <p className="font-bold">Lab 1</p>
                <button
                  onClick={launchLab}
                  className="mt-2 bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700"
                >
                  Open Python Notebook
                </button>
              </div>
            </div>
            <div className="flex items-center gap-4">
              <div className="bg-gray-200 border-2 border-dashed rounded-xl w-16 h-16" />
              <div>
                <p className="font-bold">Lab 2</p>
                <button
                  onClick={launchLab}
                  className="mt-2 bg-green-600 text-white px-3 py-1 rounded hover:bg-green-700"
                >
                  Open Python Notebook
                </button>
              </div>
            </div>
          </div>
        </section>
      )}
    </div>
  );
}

export default function Index(): JSX.Element {
  return (
    <SessionProvider>
      <HomePage />
    </SessionProvider>
  );
}
