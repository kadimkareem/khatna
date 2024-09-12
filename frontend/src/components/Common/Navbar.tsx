import React from 'react'
import { Button, Flex, Icon, useDisclosure } from '@chakra-ui/react'
import { FaPlus } from 'react-icons/fa'

import AddUser from '../Admin/AddUser'
import AddItem from '../Items/AddItem'
import AddCar from '../Cars/AddCar'  // Import the AddCar component

interface NavbarProps {
  type: string
}

const Navbar: React.FC<NavbarProps> = ({ type }) => {
  const addUserModal = useDisclosure()
  const addItemModal = useDisclosure()
  const addCarModal = useDisclosure()  // Add a disclosure for the car modal

  return (
    <>
      <Flex py={8} gap={4}>
        <Button
          variant="primary"
          gap={1}
          fontSize={{ base: 'sm', md: 'inherit' }}
          onClick={
            type === 'User'
              ? addUserModal.onOpen
              : type === 'Item'
                ? addItemModal.onOpen
                : addCarModal.onOpen  // Handle car type
          }
        >
          <Icon as={FaPlus} /> Add {type}
        </Button>
        <AddUser isOpen={addUserModal.isOpen} onClose={addUserModal.onClose} />
        <AddItem isOpen={addItemModal.isOpen} onClose={addItemModal.onClose} />
        <AddCar isOpen={addCarModal.isOpen} onClose={addCarModal.onClose} />  {/* Render AddCar component */}
      </Flex>
    </>
  )
}

export default Navbar