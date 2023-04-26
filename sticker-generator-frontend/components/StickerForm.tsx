// components/StickerForm.tsx
import { useState, ChangeEvent, FormEvent } from 'react';
import { StickerData } from '../interfaces/sticker';

const StickerForm: React.FC = () => {
  const [sticker, setSticker] = useState<string>('');
  const [size, setSize] = useState<string>('1024');
  const [number, setNumber] = useState<number>(1);
  const [result, setResult] = useState<string>('');
  const [backgroundRemovalMethod, setBackgroundRemovalMethod] = useState<string>('AI');
  const [isLoading, setIsLoading] = useState<boolean>(false);

  const handleSubmit = async (e: FormEvent) => {
    e.preventDefault();
    setIsLoading(true);
    const payload: StickerData = { sticker, size, number, remover_method: backgroundRemovalMethod };

    const response = await fetch('http://localhost:5000/generate-sticker', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    const data = await response.json();
    setResult(data.sticker_url);
    setIsLoading(false);
  };

  return (
    <div className="p-6 bg-green-200">
      <form className="bg-white p-6 rounded-lg shadow-md" onSubmit={handleSubmit}>
        <label className="block font-medium text-gray-700 mb-2">Sticker:</label>
        <input
          className="border border-gray-400 p-2 w-full"
          type="text"
          value={sticker}
          onChange={(e: ChangeEvent<HTMLInputElement>) => setSticker(e.target.value)}
        />
        <label className="block font-medium text-gray-700 mb-2 mt-4">Size:</label>
        <select
          className="border border-gray-400 p-2 w-full mt-2"
          value={size}
          onChange={(e: ChangeEvent<HTMLSelectElement>) => setSize(e.target.value)}
        >
          <option value="256">256</option>
          <option value="512">512</option>
          <option value="1024">1024</option>
        </select>
        <label className="block font-medium text-gray-700 mb-2 mt-4">
          Background Removal Method:
        </label>
        <select
          className="border border-gray-400 p-2 w-full mt-2"
          value={backgroundRemovalMethod}
          onChange={(e: ChangeEvent<HTMLSelectElement>) =>
            setBackgroundRemovalMethod(e.target.value)
          }
        >
          <option value="AI">AI</option>
          <option value="Standard">Standard</option>
        </select>
        <button
          className="bg-green-500 text-white font-medium py-2 px-4 mt-4 rounded-full hover:bg-green-600"
          type="submit"
        >
          Generate Sticker
        </button>
      </form>
      {isLoading && (
        <div className="flex justify-center mt-4">
          <div role="status" className="flex items-center">
            <svg aria-hidden="true" className="w-8 h-8 mr-2 text-gray-200 animate-spin fill-green-600" viewBox="0 0 100 101" fill="none" xmlns="http://www.w3.org/2000/svg">
              <path d="M100 50.5908C100 78.2051 77.6142 100.591 50 100.591C22.3858 100.591 0 78.2051 0 50.5908C0 22.9766 22.3858 0.59082 50 0.59082C77.6142 0.59082 100 22.9766 100 50.5908ZM9.08144 50.5908C9.08144 73.1895 27.4013 91.5094 50 91.5094C72.5987 91.5094 90.9186 73.1895 90.9186 50.5908C90.9186 27.9921 72.5987 9.67226 50 9.67226C27.4013 9.67226 9.08144 27.9921 9.08144 50.5908Z" fill="currentColor"/>
              <path d="M93.9676 39.0409C96.393 38.4038 97.8624 35.9116 97.0079 33.5539C95.2932 28.8227 92.871 24.3692 89.8167 20.348C85.8452 15.1192 80.8826 10.7238 75.2124 7.41289C69.5422 4.10194 63.2754 1.94025 56.7698 1.05124C51.7666 0.367541 46.6976 0.446843 41.7345 1.27873C39.2613 1.69328 37.813 4.19778 38.4501 6.62326C39.0873 9.04874 41.5694 10.4717 44.0505 10.1071C47.8511 9.54855 51.7191 9.52689 55.5402 10.0491C60.8642 10.7766 65.9928 12.5457 70.6331 15.2552C75.2735 17.9648 79.3347 21.5619 82.5849 25.841C84.9175 28.9121 86.7997 32.2913 88.1811 35.8758C89.083 38.2158 91.5421 39.6781 93.9676 39.0409Z" fill="currentFill"/>
            </svg>
            <span className="sr-only">Loading...</span>
          </div>
        </div>
      )}
      {result && !isLoading && (
        <img src={result} alt="Generated Sticker" className="mt-4" />
      )}
    </div>
  );
  };
  
  export default StickerForm;
  